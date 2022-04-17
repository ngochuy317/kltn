from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View


# Create your views here.
class Cart(LoginRequiredMixin, View):
    template_name = "order/shopping-cart.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class Payment(LoginRequiredMixin, View):
    template_name = "order/payment.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
