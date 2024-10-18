from django.urls import path
from . import views

urlpatterns = [
    path('create-product/', views.create_product, name='create_product'),
    path('product-price/<int:product_id>/', views.product_price, name='product_price'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('product-list/', views.product_list, name='product_list'),
    path('product-detail/<int:product_id>/', views.product_detail, name='product_detail'),  # Para ver detalles del product
]
