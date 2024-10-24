class Product:
    """Класс для представления товара"""

    name: str
    description: str
    price: float
    quantity: int
    cost: float

    product_list = []
    product_name_list = []

    def __init__(self, name, description, price, quantity, cost=0):
        """Метод для инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.cost = price * quantity

    def __add__(self, other):
        """Магический метод для сложения стоимости товаров"""
        return self.cost + other.cost

    def __str__(self):
        """Магический метод для строкового отображения класса Product"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, product_dict):
        """Класс-метод для создания нового экземпляра класса из словаря с проверкой на дубликаты"""
        name = product_dict.get("name")
        description = product_dict.get("description")
        price = product_dict.get("price")
        quantity = product_dict.get("quantity")
        if name in cls.product_name_list:
            for product in cls.product_list:
                if product.name == name:
                    product.quantity += product_dict.get("quantity")
                    product.price = max(product.price, product_dict.get("price"))
                    return product
        new_product = cls(name=name, description=description, price=price, quantity=quantity)
        cls.product_list.append(new_product)
        cls.product_name_list.append(new_product.name)
        return new_product

    @property
    def price(self):
        """Геттер для приватного атрибута цены"""
        return self.__price

    @price.setter
    def price(self, new_price: int):
        """Сеттер для приватного атрибута цены, позволяющий его изменять, с проверкой
        на положительные и ненулевые значения"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price
