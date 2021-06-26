from django.db import transaction
from django.core.exceptions import ValidationError
from rest_framework import generics, viewsets, mixins, permissions

from .models import Currency, Order
from .serializers import CurrencySerializer, OrderSerializer
from .filters import OrderFilters
from .paginators import OrderPaginator
from accounts.models import Account


class CurrencyView(generics.ListAPIView):
    """
    API endpoint that allows listing currencies, in alphabetical order
    """
    queryset = Currency.objects.all().order_by('id')
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticated]

    search_fields = ['identifier']

class OrderViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows listing and creating orders
    """
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    pagination_class = None
    #pagination_class = OrderPaginator

    filterset_class = OrderFilters

    def perform_create(self, serializer):
        with transaction.atomic():
            result = serializer.save()
            result.seller_account.balance -= result.amount
            result.seller_account.save()
            return result

    def perform_destroy(self, instance):
        with transaction.atomic():
            if self.request.user == instance.seller_account.user:
                instance.seller_account.balance += instance.amount
                instance.seller_account.save()
                instance.delete()
            else:
                buy_account = Account.objects.filter(user = self.request.user, currency = instance.currency).first()
                if not buy_account:
                    raise ValidationError("no appropriate account for buying found")
                if buy_account.balance < instance.price:
                    raise ValidationError("insufficient funds to buy")
                increment_account, _created = Account.objects.get_or_create(
                    user = self.request.user,
                    currency = instance.seller_account.currency,
                )
                seller_increment_account, _created = Account.objects.get_or_create(
                    user = instance.seller_account.user,
                    currency = instance.currency
                )
                increment_account.balance += instance.amount
                seller_increment_account.balance += instance.price
                buy_account.balance -= instance.price
                instance.delete()
                increment_account.save()
                seller_increment_account.save()
                buy_account.save()
