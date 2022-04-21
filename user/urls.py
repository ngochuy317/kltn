from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('signin/', SignIn.as_view(), name='signin'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('signout/', SignOut.as_view(), name='signout'),
    path('activate/<str:uidb64>/<str:token>/', activate, name='activate'),
    path('profile/', Profile.as_view(), name='profile'),
    path('change-password/', ChangePassword.as_view(), name='change-password'),
]