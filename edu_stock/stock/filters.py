from django_filters import rest_framework as filters

from .models import Order

class OrderFilters(filters.FilterSet):
    sell_currency = filters.CharFilter(field_name = "seller_account__currency__identifier")
    buy_currency = filters.CharFilter(field_name = "currency__identifier")
    price = filters.RangeFilter()

    class Meta:
        model = Order
        fields = ['sell_currency', 'buy_currency', 'price', 'amount']