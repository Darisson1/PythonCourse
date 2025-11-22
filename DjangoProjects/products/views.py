from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
# index for the main page


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products' : products})

def new_products(request):
    return HttpResponse('These are the new products')