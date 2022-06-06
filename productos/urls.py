from django.urls import path

from productos.views import market


urlpatterns = [
    path('', market, name = 'store'),
]