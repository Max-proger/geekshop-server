from django.shortcuts import render
import json
import datetime
from  products.models import ProductCategory, Product


# Create your views here.

def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
        'time': datetime.datetime.now(),
    }

    return render(request, 'products/products.html', context)
