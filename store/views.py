from django.shortcuts import render

# Create your views here.
def store_home (req):
    return render(req, 'store/store.html')