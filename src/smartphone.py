from src.product import Product


class Smartphone(Product):
    """Класс для представления товаров, относящихся к категории 'Смартфон'"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color, cost=0):
        super().__init__(name, description, price, quantity, cost=0)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Магический метод для сложения стоимости товаров"""
        if type(other) is Smartphone:
            return self.cost + other.cost
        raise TypeError
