from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'product'

urlpatterns = [
    path('productdetail/<slug:slug>/', ProductDetail.as_view(), name='productdetail'),
    path('product/', ProductView.as_view(), name='product'),
    path('product/filter/<str:category>', ProductView.as_view(), name='productfilter'),
    path('product/search/', ProductSearch.as_view(), name='productsearch'),
]
