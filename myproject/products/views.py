# products/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .services import ProductService
from .models import Product 
from django.contrib.auth.decorators import login_required
from .forms import ProductForm

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ProductForm()

    return render(request, 'create_product.html', {'form': form})

# products/views.py

from django.shortcuts import render, get_object_or_404
from .models import Product
from .services import ProductService

@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    base_price = product.price
    user_price = ProductService.calculate_price(request.user, base_price)

    return render(request, 'product_detail.html', {
        'product': product,
        'base_price': base_price,
        'user_price': user_price
    })

@login_required
def product_list(request):
    products = Product.objects.all()
    product_prices = []
    for product in products:
        base_price = product.price
        user_price = ProductService.calculate_price(request.user, base_price)
        product_prices.append({'product': product, 'user_price': user_price})

    return render(request, 'product_list.html', {'product_prices': product_prices})

@login_required
def product_price(request, product_id):
    product = Product.objects.get(id=product_id)
    calculated_price = ProductService.calculate_price(request.user, product.price)
    return render(request, 'product_price.html', {'product': product, 'price': calculated_price})

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart = request.session.get('cart', [])
    cart.append(product.id)
    request.session['cart'] = cart
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)
    total_price = 0
    products_with_prices = []
    for product in products:
        base_price = product.price
        user_price = ProductService.calculate_price(request.user, base_price)
        products_with_prices.append({
            'product': product,
            'user_price': user_price
        })
        total_price += user_price

    return render(request, 'cart.html', {
        'products': products_with_prices,
        'total_price': total_price
    })
