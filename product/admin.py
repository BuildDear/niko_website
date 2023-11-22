from django.contrib import admin

# Register your models here.

from product.models import ProductCategory, Product

admin.site.register(Product)
admin.site.register(ProductCategory)


