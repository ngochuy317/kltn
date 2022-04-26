from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from product.models import Product

from .models import Cart, Order, OrderDetail


# Create your views here.
class CartView(LoginRequiredMixin, View):
    template_name = "order/shopping-cart.html"
    
    def get(self, request, *args, **kwargs):
        carts = Cart.objects.filter(
            user=request.user
        )

        cart_price_total = sum([i.get_total_price for i in carts])

        context = {
            "carts": carts,
            "cart_price_total": cart_price_total,
        }
        return render(request, self.template_name, context)


class PaymentView(LoginRequiredMixin, View):
    template_name = "order/payment.html"
    
    def get(self, request, *args, **kwargs):
        carts = Cart.objects.filter(
            user=request.user)
        cart_price_total = sum([i.get_total_price for i in carts])
        
        context = {
            "carts": carts,
            "cart_price_total": cart_price_total,
        }
            
        return render(request, self.template_name, context)

class CheckOutView(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        carts = Cart.objects.filter(
            user=request.user)

        total_price = 0
        order = Order.objects.create(
            user=request.user
        )
        for item in carts:
            total_price += item.get_total_price
            OrderDetail.objects.create(
                product=item.product,
                price=item.product.price,
                quantity=item.quantity,
                order=order
            )
            item.delete()

        order.total_order = total_price
        order.save()
            
        return redirect('home:index')


class AddToCart(LoginRequiredMixin, View):
    template_name = "order/shopping-cart.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get("id")
        quantity = request.POST.get("quantity")
        product = Product.objects.filter(id=product_id).first()
        carts = Cart.objects.filter(
            user=request.user,
            product=product
        )
        cart = carts.first()

        if cart is None:
            cart = Cart.objects.create(
                user=request.user,
                product=product,
                quantity=quantity
            )
        else:
            cart.quantity = quantity
            cart.save()
        context = {}
        response = JsonResponse(context)
        return response


class RemoveItemToCart(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        id = request.POST.get('id')
        product = Product.objects.filter(id=id).first()
        
        Cart.objects.filter(
            user=request.user,
            product=product,
        ).delete()

        carts = Cart.objects.filter(
            user=request.user
        )

        no_item_in_carts = len(carts)
        cart_price_total = sum([i.get_total_price for i in carts])

        context = {
            "no_item_in_carts": no_item_in_carts,
            "cart_price_total": cart_price_total,
        }
        response = JsonResponse(context)
        return response
