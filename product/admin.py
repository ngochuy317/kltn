from django import forms
from django.contrib import admin
from .models import Category, Product, ProductSlider


# Register your models here.
class EProductSliderModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['product'].queryset = Product.objects.all()


class ProductSliderInline(admin.ModelAdmin):
    form = EProductSliderModelForm
    filter_horizontal = ('product',)

    def has_add_permission(self, request, obj=None):
        return False


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount',)
    

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductSlider, ProductSliderInline)
