from django.shortcuts import render
from django.views.generic import View

from product.models import Product


# Create your views here.
class Index(View):
    template_name = "home/index.html"

    def get(self, request, *args, **kwargs):
        slider_products = Product.objects.distinct().filter(productslider__id=1)
        recent_products = Product.objects.order_by('-create_at')[:3]
        discount_book = Product.objects.filter(have_discount=True)[:8]
        context = {
            'slider_products': slider_products,
            'recent_products': recent_products,
            'title': "Home Page",
            "discount_book": discount_book,
        }
        return render(request, self.template_name, context)


class Contact(View):
    template_name = "home/contact.html"

    def get(self, request, *args, **kwargs):
        context = {
            'title': "Contact"
        }
        return render(request, self.template_name, context)
