from rest_framework import generics
from rest_framework import permissions

from .models import Account
from .serializers import AccountSerializer


class AccountView(generics.ListAPIView):
    """
    API endpoint that allows listing accounts
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AccountSerializer

    def get_queryset(self):
        user = self.request.user
        return Account.objects.filter(user=user)