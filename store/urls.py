from django.urls import path
from . import views
app_name = 'store'

urlpatterns = [
        path('', views.store_home, name = 'store_home'),
        path('<slug:category_slug>/', views.store_home, name='products_by_category'),
        path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
]