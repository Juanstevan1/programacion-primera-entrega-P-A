from .services import OrderService
from .models import Order
from products.services import ProductService

class OrderFacade:
    def __init__(self, user, cart=None):
        self.user = user
        self.cart = cart

    def place_order(self):
        """
        Llamamos al servicio para crear la orden
        """
        if not self.cart:
            raise ValueError("El carrito está vacío")
        
        order = OrderService.create_order(self.user, self.cart)
        return order

    def get_user_orders(self):
        """
        Recupera todas las órdenes de un usuario.
        """
        return Order.objects.filter(user=self.user)
    
    def get_user_orders_with_prices(self):
        """
        Devuelve las órdenes con los precios calculados para el usuario.
        """
        orders = self.get_user_orders()
        orders_with_prices = []

        for order in orders:
            products_with_prices = []
            for product in order.products.all():
                user_price = ProductService.calculate_price(self.user, product.price)
                products_with_prices.append({'product': product, 'user_price': user_price})

            orders_with_prices.append({
                'order': order,
                'products_with_prices': products_with_prices,
                'total_price': sum([item['user_price'] for item in products_with_prices])
            })

        return orders_with_prices
    
    def get_order_detail(self, order_id):
        return Order.objects.get(id=order_id, user=self.user)

