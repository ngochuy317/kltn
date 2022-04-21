from django.conf import settings

from django.contrib.auth.hashers import check_password
from .models import CustomUser


class AdminAuthBackend(object):
    def authenticate(self, request, username=None, password = None):
        try:
            user = CustomUser.objects.get(username = username)

            if user.password == password:
                return user

        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return None
