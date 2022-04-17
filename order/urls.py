from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'order'

urlpatterns = [
    path('shopping-cart/', Cart.as_view(), name='cart'),
    path('payment/', Cart.as_view(), name='payment'),
]