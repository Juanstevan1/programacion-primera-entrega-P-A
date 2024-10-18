from .models import Product

class ProductBuilder:
    def __init__(self):
        self.product = Product()

    def set_name(self, name):
        self.product.name = name
        return self

    def set_color(self, color):
        self.product.color = color
        return self

    def set_size(self, size):
        self.product.size = size
        return self

    def set_price(self, price):
        self.product.price = price
        return self

    def build(self):
        self.product.save()
        return self.product