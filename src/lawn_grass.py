from src.product import Product


class LawnGrass(Product):
    """Класс для представления товаров, относящихся к категории 'Трава газонная'"""

    def __init__(self, name, description, price, quantity, country, germination_period, color, cost=0):
        super().__init__(name, description, price, quantity, cost=0)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Магический метод для сложения стоимости товаров"""
        if type(other) is LawnGrass:
            return self.cost + other.cost
        raise TypeError
