from django.db import models
from django.template.defaultfilters import slugify
from django.utils.functional import cached_property

from .utils import remove_accents


# Create your models here.
class Category(models.Model):

    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to = 'images/categories/%Y-%m-%d/', blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def  __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.title) + "-" + str(self.id)
            self.save()


class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'images/products/%Y-%m-%d/')
    price = models.FloatField()
    amount = models.IntegerField()
    avg_rating = models.IntegerField(null=True, blank=True, default=0)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    have_discount = models.BooleanField(default=False)
    discount_price = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.name) + "-" + str(self.id)
            self.save()

    def __str__(self):
        return self.name

    @property
    def search_name(self):
        return remove_accents(self.name)


class ProductSlider(models.Model):
    product = models.ManyToManyField(Product, related_name='productslider')

    def __str__(self) -> str:
        return "ProdcutSlider"
