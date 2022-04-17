from django.db import models

from user.models import CustomUser


# Create your models here.
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


class OrderDetail(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'images/products/%Y-%m-%d/')
    amount = models.FloatField()
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')

    @property
    def total_amount(self):
        return self.amount * self.quantity
