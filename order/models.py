from django.utils import timezone
from django.db import models
from product.models import Product
from user.models import User
from payment.models import Payment


class Shipping(models.Model):
    city = models.CharField(max_length=50, default="Lviv")
    region = models.CharField(max_length=100, default="Lviv")
    post_id = models.BigIntegerField(default=123)

    class Meta:
        db_table = 'shipping'


class Basket(models.Model):
    METHOD_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    payment = models.ForeignKey(to=Payment, on_delete=models.SET_NULL, default=None, null=True)
    shipping = models.ForeignKey(to=Shipping, on_delete=models.SET_NULL, default=None, null=True)
    website_user = models.ForeignKey(to=User, on_delete=models.SET_NULL, default=None, null=True)
    status = models.CharField(max_length=100, choices=METHOD_CHOICES, default="pending")
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'basket'


class ProductDetail(models.Model):
    quantity_sell = models.IntegerField()
    product = models.ForeignKey(to=Product, on_delete=models.SET_NULL, null=True, default=None)
    basket = models.ForeignKey(to=Basket, on_delete=models.SET_NULL, null=True, default=None)

    class Meta:
        db_table = 'product_detail'

