from django.shortcuts import render
from .models import Product

# Create your views here.
def store_home (req):
    products = Product.objects.all().filter(is_available=True)
    no_of_products = products.count()
    context = {
        'products':products, 
        'no_of_products':no_of_products
    }
    return render(req, 'store/store.html', context)