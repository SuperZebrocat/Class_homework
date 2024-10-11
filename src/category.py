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
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0
