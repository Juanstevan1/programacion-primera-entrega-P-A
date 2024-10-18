from django.shortcuts import render, redirect
from .facades import OrderFacade
from products.services import ProductService
from products.models import Product
from django.contrib.auth.decorators import login_required
from .models import Order
from django.shortcuts import render, get_object_or_404
from .models import Order

@login_required
def create_order(request):
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)

    if not products.exists():
        return redirect('product_list')

    order_facade = OrderFacade(user=request.user, cart=products)
    order = order_facade.place_order()

    request.session['cart'] = []

    return redirect('order_detail', order_id=order.id)

@login_required
def user_orders(request):
    order_facade = OrderFacade(user=request.user)
    orders_with_prices = order_facade.get_user_orders_with_prices()

    return render(request, 'user_orders.html', {
        'orders_with_prices': orders_with_prices,
        'user': request.user
    })

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    products_with_prices = []
    for product in order.products.all():
        user_price = ProductService.calculate_price(request.user, product.price)
        products_with_prices.append({
            'product': product,
            'user_price': user_price
        })

    total_price = sum([item['user_price'] for item in products_with_prices])
    
    return render(request, 'order_detail.html', {
        'order': order,
        'products_with_prices': products_with_prices,
        'total_price': total_price
    })
