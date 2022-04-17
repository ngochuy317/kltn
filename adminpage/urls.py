from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'adminpage'

urlpatterns = [
    path('usermanagement/', UserManagement.as_view(), name='usermanagement'),
    path('ordermanagement/', OrderManagement.as_view(), name='ordermanagement'),
    path('productmanagement/', ProductManagement.as_view(), name='productmanagement'),
    path('vouchermanagement/', VoucherManagement.as_view(), name='vouchermanagement'),
    path('statistic/', Statistic.as_view(), name='statistic'),
]