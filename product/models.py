from django.utils import timezone
from django.db import models

from user.models import TelegramAdmin


class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta():
        db_table = 'product_category'


class Product(models.Model):
    admin = models.ForeignKey(to=TelegramAdmin, on_delete=models.SET_NULL, default=None, null=True, blank=True)
    animal = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=0)
    photo = models.ImageField(upload_to='products_images')
    isShown = models.BooleanField()
    upload_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.SET_NULL, default=None, null=True, blank=True)

    class Meta():
        db_table = 'website_product'

    def __str__(self):
        return f'Product: {self.name} / Category: {self.category}'
