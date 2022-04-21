from django.db import models

from user.models import CustomUser
from product.models import Product


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    mode = models.IntegerField(default=0, choices=(
        (0, "Chưa đặt"),
        (1, "Đã đặt"),
        (2, "Đã chấp nhận"),
        (3, "Đã nhận hàng"),
    ))
    day_update = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user}--{self.product}--{self.quantity}"

    @property
    def get_total_price(self):
        return self.quantity * self.product.price

    
class Order(models.Model):
    STATUS_CHOICES = (
        ("OD", "Đặt hàng"),
        ("WFC", "Chờ xác nhận"),
        ("PK", "Đóng gói bàn giao"),
        ('SU', 'Thành công'),
        ('FA', 'Thất bại'),
    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="OD")
    created_at = models.DateTimeField(auto_now_add=True)
    total_order = models.IntegerField(default=0)


class OrderDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")
    price = models.FloatField()
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')

    @property
    def total_amount(self):
        return self.price * self.quantity
