from .strategies import RegularUserPriceStrategy, PremiumUserPriceStrategy, WholesaleUserPriceStrategy
from decimal import Decimal, InvalidOperation
from .models import Product

class ProductService:
    
    @staticmethod
    def create_product(data):
        try:
            # Convertimos el valor del precio a Decimal
            price = Decimal(data.get('price'))
        except InvalidOperation:
            # Si hay un error en la conversión, lanzamos una excepción o manejamos el error
            raise ValueError("El valor del precio no es válido. Por favor, introduce un número válido.")
        
        product = Product.objects.create(
            name=data.get('name'),
            color=data.get('color'),
            size=data.get('size'),
            price=price  # Usamos el precio convertido a Decimal
        )
        return product

    @staticmethod
    def calculate_price(user, base_price):
        """
        Aplica la estrategia de precio adecuada según el tipo de usuario.
        :param user: Objeto del usuario.
        :param base_price: Precio base del producto.
        :return: Precio calculado.
        """
        # Obtener el tipo de usuario desde el perfil
        user_type = user.profile.user_type

        if user_type == 'premium':
            strategy = PremiumUserPriceStrategy()
        elif user_type == 'wholesale':
            strategy = WholesaleUserPriceStrategy()
        else:
            strategy = RegularUserPriceStrategy()

        return strategy.calculate(base_price)
