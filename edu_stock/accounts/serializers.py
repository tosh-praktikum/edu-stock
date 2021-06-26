from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Account


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['user', 'currency', 'balance']