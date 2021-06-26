from django.core.exceptions import ValidationError
from rest_framework import serializers

from .models import Currency, Order


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['name', 'identifier']


class OrderSerializer(serializers.ModelSerializer):
    sell_currency = serializers.CharField(source = "seller_account.currency.identifier")
    buy_currency = serializers.CharField(source = "currency.identifier")

    class Meta:
        model = Order
        fields = ['id', 'sell_currency', 'amount', 'buy_currency', 'price']

    def validate(self, attrs):
        sell_currency = attrs['seller_account']['currency']['identifier']
        sell_account = self.context['request'].user.accounts.filter(currency__identifier=sell_currency).first()
        if not sell_account:
            raise ValidationError("no valid seller account found")
        if sell_account.balance < attrs['amount']:
            raise ValidationError("insufficient funds on seller account")
        attrs['seller_account'] = sell_account
        buy_currency = Currency.objects.get(identifier=attrs['currency']['identifier'])
        if not buy_currency:
            raise ValidationError("invalid buy currency sent")
        attrs['currency'] = buy_currency
        return super().validate(attrs)