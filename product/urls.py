from django.urls import path
from product.views import products
from order.views import order_add, order_remove

app_name = 'product'

urlpatterns = [
   path('', products, name='index'),
   path('orders/add/<int:product_id>/', order_add, name='order_add'),
   path('orders/remove/<int:order_id>/', order_remove, name='order_remove'),
]
