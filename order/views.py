from product.models import Product
from order.models import Basket
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required
def order_add(request, product_id):
    product = Product.objects.get(id=product_id)
    orders = Basket.objects.filter(user=request.user, product=product)

    if not orders.exists():
        Basket.objects.create(user=request.user, product=product, quantity_sell=1)
    else:
        order = orders.first()
        order.quantity_sell += 1
        order.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def order_remove(request, order_id):
    order = Basket.objects.get(id=order_id)
    order.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])