import json
import os

from src.category import Category
from src.product import Product

PATH_FILE = os.path.abspath("../data/products.json")


def read_json(path_file: str) -> list[dict]:
    """Функция для получения данных о товарах из JSON-файла"""
    full_path = os.path.abspath(path_file)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: list[dict]):
    """Функция получения экземпляров класса из JSON-файла"""
    categories = []
    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))
    return categories
