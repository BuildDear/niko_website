from django.shortcuts import render, HttpResponseRedirect
from product.models import ProductCategory, Product
from order.models import Basket

def index(request):
    return render(request, 'products/index.html')


def products(request):
    context = {
        'title': 'Store-catalog',
        'product': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
