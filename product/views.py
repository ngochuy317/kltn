from django.shortcuts import render
from django.views.generic import View

from .models import Product, Category
from .utils import remove_accents


# Create your views here.
class ProductDetail(View):
    template_name = "product/product-detail.html"

    def get(self, request, *args, **kwargs):
        slug = kwargs.get("slug")
        product = Product.objects.filter(slug=slug).first()
        title = product.name
        context = {
            "product": product,
            "title": title
        }
        return render(request, self.template_name, context)


class ProductView(View):
    template_name = "product/products.html"

    def get(self, request, *args, **kwargs):

        products = Product.objects.all()
        categories = Category.objects.all()
        if kwargs.get("category"):
            category = Category.objects.filter(title=kwargs.get("category")).first()
            products = products.filter(category=category)
        context = {
            "products": products,
            "title": "Products",
            "categories": categories,
        }
        return render(request, self.template_name, context)


class ProductSearch(View):
    template_name = "product/products.html"

    def post(self, request, *args, **kwargs):

        products = Product.objects.all()
        categories = Category.objects.all()
        user_search = request.POST.get('user_search')
        if user_search:
            user_search = remove_accents(user_search)
            products = [x for x in products if user_search in x.search_name]

        context = {
            "products": products,
            "title": "Products",
            "categories": categories
        }
        return render(request, self.template_name, context)
