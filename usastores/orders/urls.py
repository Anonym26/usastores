from django.urls import path

from .views import *

app_name = 'orders'


urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('orders_user/', order_show, name='orders_user'),
]