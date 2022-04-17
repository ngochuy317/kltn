from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'home'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('contact/', Contact.as_view(), name='contact'),
]