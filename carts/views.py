from django.shortcuts import render, redirect
from store.models import Product
from carts.models import Cart, CartItem
from django.http import HttpResponse
# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart :
        cart = request.session.create()
    
    return cart

def add_cart (request, product_id):
    product = Product.objects.get(id=product_id)
    try :
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id = _cart_id(request))
        cart.save()

    try :
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()

    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            cart = cart, 
            quantity = 1
        )
        cart_item.save()
    
    return redirect('cart')



def cart (request, total = 0, quantity= 0):
    try :
        cart = Cart.objects.filter(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart = cart, is_active= True)
        # https://www.youtube.com/watch?v=1qg9OwrmGaw&t=2417s 4:12:18
    
    except Exception as e:
        pass
    
    context = {

    }

    return render(request, 'store/cart.html', context)

