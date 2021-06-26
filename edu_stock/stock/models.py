from django.db import models
from django.core.validators import RegexValidator


class Currency(models.Model):
    name = models.CharField(unique = True, max_length = 255)
    identifier = models.CharField(max_length = 4, validators = [RegexValidator(regex = r'^\w{2,4}$', message = 'Identifier length has to be 2-4 characters in length')], primary_key = True)


class Order(models.Model):
    seller_account = models.ForeignKey('accounts.Account', related_name = "sell_orders", on_delete = models.CASCADE)
    amount = models.DecimalField(decimal_places = 2, max_digits = 20)
    currency = models.ForeignKey('stock.Currency', related_name="buy_orders", on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=20)