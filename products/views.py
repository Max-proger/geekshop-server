from django.shortcuts import render
import json
import datetime


# Create your views here.

def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request):
    context = {'title': 'GeekShop - Каталог'}
    with open('products/fixtures/goods.json', encoding='utf-8') as json_file:
        context['products'] = json.load(json_file)
    context['time'] = datetime.datetime.now()
    return render(request, 'products/products.html', context)
