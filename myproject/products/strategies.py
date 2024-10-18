from decimal import Decimal

class PriceStrategy:
    def calculate(self, product_price):
        raise NotImplementedError("This method should be overridden")

class RegularUserPriceStrategy(PriceStrategy):
    def calculate(self, product_price):
        return product_price  # No discount

class PremiumUserPriceStrategy(PriceStrategy):
    def calculate(self, product_price):
        return product_price * Decimal('0.9')  # 10% discount

class WholesaleUserPriceStrategy(PriceStrategy):
    def calculate(self, product_price):
        return product_price * Decimal('0.8')  # 20% discount
