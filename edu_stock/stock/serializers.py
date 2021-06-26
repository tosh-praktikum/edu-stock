from rest_framework import serializers

from .models import Currency, Order


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['name', 'identifier']


class OrderSerializer(serializers.ModelSerializer):
    sell_currency = serializers.PrimaryKeyRelatedField(read_only = True, source = "seller_account.currency")
    class Meta:
        model = Order
        fields = ['sell_currency', 'amount', 'currency', 'price']