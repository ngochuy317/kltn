from django.shortcuts import render
from django.views.generic import View

from user.models import CustomUser


# Create your views here.
class UserManagement(View):
    template_name = "adminpage/Manage-User.html"

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        context = {
            'users': users,
            'route': 'usermanagement'
        }
        return render(request, self.template_name, context)


class OrderManagement(View):
    template_name = "adminpage/Manage-Order.html"

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        context = {
            'users': users,
            'route': 'ordermanagement'
        }
        return render(request, self.template_name, context)


class ProductManagement(View):
    template_name = "adminpage/Manage-Product.html"

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        context = {
            'users': users,
            'route': 'productmanagement'
        }
        return render(request, self.template_name, context)


class VoucherManagement(View):
    template_name = "adminpage/Manage-Voucher.html"

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        context = {
            'users': users,
            'route': 'vouchermanagement'
        }
        return render(request, self.template_name, context)


class Statistic(View):
    template_name = "adminpage/Statistics.html"

    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        context = {
            'users': users,
            'route': 'statistics'
        }
        return render(request, self.template_name, context)
