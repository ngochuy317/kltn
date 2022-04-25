from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'order'

urlpatterns = [
    path('add-to-cart/', AddToCart.as_view(), name='add-to-cart'),
    path('remove_item_in_cart/', RemoveItemToCart.as_view(), name='remove_item_in_cart'),
    path('shopping-cart/', CartView.as_view(), name='cart'),
    path('payment/', PaymentView.as_view(), name='payment'),
]