from src.product import Product


class Category:
    """Класс для представления категории товаров"""

    category_count = 0
    product_count = 0

    name: str
    description: str
    products: list

    def __init__(self, name, description, products=None):
        """Метод для инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        """Магический метод для строкового отображения класса Category"""
        quantity_list = []
        for product in self.__products:
            quantity_list.append(product.quantity)
        quantity_sum = sum(quantity_list)
        return f"{self.name}, количество продуктов: {quantity_sum} шт."

    def add_product(self, product: Product):
        """Метод добавления продуктов в категории товаров"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Свойство класса, позволяющее выводить список продуктов в виде строки"""
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    @property
    def products_in_list(self):
        """Геттер для приватного атрибута списка продуктов"""
        return self.__products
