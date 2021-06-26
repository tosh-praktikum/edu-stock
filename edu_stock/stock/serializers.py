from rest_framework import serializers

from .models import Currency, Order


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['name', 'identifier']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['account', 'amount', 'currency', 'price']