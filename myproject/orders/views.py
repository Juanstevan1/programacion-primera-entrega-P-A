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
    # Obtener el carrito de la sesión del usuario
    cart = request.session.get('cart', [])
    
    # Recuperar los productos del carrito
    products = Product.objects.filter(id__in=cart)

    if not products.exists():
        # En caso de que el carrito esté vacío, redirigir al listado de productos o mostrar un mensaje
        return redirect('product_list')

    # Usar el facade para crear la orden
    order_facade = OrderFacade(user=request.user, cart=products)
    order = order_facade.place_order()

    # Vaciar el carrito después de crear la orden
    request.session['cart'] = []

    # Redirigir al detalle de la orden
    return redirect('order_detail', order_id=order.id)


@login_required
def user_orders(request):
    # Usamos el Facade para obtener las órdenes del usuario actual y calcular los precios
    order_facade = OrderFacade(user=request.user)
    orders_with_prices = order_facade.get_user_orders_with_prices()

    # Renderizamos la plantilla con las órdenes y los precios ajustados
    return render(request, 'user_orders.html', {
        'orders_with_prices': orders_with_prices,
        'user': request.user
    })


@login_required
def order_detail(request, order_id):
    # Usamos el facade para obtener los detalles de la orden
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    # Crear una lista de productos con los precios calculados basados en el tipo de usuario
    products_with_prices = []
    for product in order.products.all():
        # Calculamos el precio basado en el tipo de usuario
        user_price = ProductService.calculate_price(request.user, product.price)
        products_with_prices.append({
            'product': product,
            'user_price': user_price
        })

    # Calcular el precio total basado en los precios ajustados
    total_price = sum([item['user_price'] for item in products_with_prices])
    
    return render(request, 'order_detail.html', {
        'order': order,
        'products_with_prices': products_with_prices,
        'total_price': total_price
    })