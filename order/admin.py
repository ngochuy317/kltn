from django.contrib import admin
from .models import Order, OrderDetail


# Register your models here.
class OrderDetailInline(admin.TabularInline):
    model = OrderDetail
    # fk_name = "order"

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderDetailInline]
