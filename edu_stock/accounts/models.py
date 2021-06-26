from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Account(models.Model):
    user = models.ForeignKey(to = User, on_delete = models.CASCADE, related_name = "accounts")
    currency = models.ForeignKey(to = 'stock.Currency', on_delete = models.CASCADE)
    balance = models.DecimalField(decimal_places = 2, max_digits = 20)