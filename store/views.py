from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Product
from category.models import Category

def store_home (req, category_slug=None):
    category = None
    products = None

    if category_slug!=None:
        category = get_object_or_404(Category, slug=category_slug)        
        products = category.products.all().filter(is_available=True)
        no_of_products = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        no_of_products = products.count()

    context = {
        'products':products, 
        'no_of_products':no_of_products
    }
    return render(req, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try :
        single_product = Product.objects.get(slug=product_slug)
    except Exception as e:
        return e
    
    context = {
        'single_product':single_product
    }
    return render(request, 'store/product-detail.html', context)


