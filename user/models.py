from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, username, password=None):

        if username is None:
            raise TypeError('Users must have username.')

        user = self.model(username=username)
        user.set_password(password)
        user.is_active = True
        user.save()

        return user

    def create_superuser(self, username, password):

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.is_active = True
        user.save()

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    SEX_CHOICES = (
        ("Nam", "Nam"),
        ("Nữ", "Nữ"),
        ("-", "-")
    )

    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    fullname = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to ='media/user/avatar/%Y/%m/%d', blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, default="-")
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    def __str__(self) -> str:
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

