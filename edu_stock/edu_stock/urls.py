from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework import routers

from stock.views import CurrencyView, OrderViewSet
from accounts.views import AccountView


router = routers.DefaultRouter()
router.register('orders', OrderViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('currencies', CurrencyView.as_view()),
    path('accounts', AccountView.as_view()),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
