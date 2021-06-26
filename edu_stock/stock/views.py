from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions

from .models import Currency, Order
from .serializers import CurrencySerializer, OrderSerializer
from .filters import OrderFilters
from .paginators import OrderPaginator


class CurrencyView(generics.ListAPIView):
    """
    API endpoint that allows listing currencies, in alphabetical order
    """
    queryset = Currency.objects.all().order_by('id')
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticated]

    search_fields = ['identifier']

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows listing and creating orders
    """
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    pagination_class = None
    #pagination_class = OrderPaginator

    filterset_class = OrderFilters
