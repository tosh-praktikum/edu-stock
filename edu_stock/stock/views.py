from rest_framework import generics
from rest_framework import permissions

from .models import Currency, Order
from .serializers import CurrencySerializer, OrderSerializer


class CurrencyView(generics.ListAPIView):
    """
    API endpoint that allows listing currencies, in alphabetical order
    """
    queryset = Currency.objects.all().order_by('id')
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderView(generics.ListCreateAPIView):
    """
    API endpoint that allows listing and creating orders
    """
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]