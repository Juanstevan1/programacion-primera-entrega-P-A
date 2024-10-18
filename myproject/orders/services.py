# orders/services.py
from .models import Order
from products.models import Product
from products.services import ProductService

class OrderService:

    @staticmethod
    def create_order(user, cart):
        total_price = OrderService.calculate_total_price(user, cart)
        order = Order(user=user, total_price=total_price)
        order.save()
        order.products.set(cart)
        return order

    @staticmethod
    def calculate_total_price(user, cart):
        total_price = 0
        for product in cart:
            user_price = ProductService.calculate_price(user, product.price)
            total_price += user_price
        return total_price

    @staticmethod
    def get_order_by_id(order_id):
        return Order.objects.get(id=order_id)
