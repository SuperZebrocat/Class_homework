import pytest

from src.category import Category


def test_category_init(category1, category2):
    assert category1.name == "Смартфоны"
    assert category1.description == "Средство коммуникации"
    assert len(category1.products_in_list) == 3

    assert category1.category_count == 2
    assert category2.category_count == 2
    assert Category.category_count == 2

    assert category1.product_count == 4
    assert category2.product_count == 4
    assert Category.product_count == 4


def test_add_product(category1, test_product):
    category1.add_product(test_product)
    assert category1.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\nIphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
    )


def test_products_property(category1):
    assert category1.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\nXiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_products_in_list_property(category1, test_product):
    assert len(category1.products_in_list) == 3
    category1.add_product(test_product)
    assert len(category1.products_in_list) == 4


def test_category_str(category1):
    assert str(category1) == "Смартфоны, количество продуктов: 27 шт."


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(product_iterator).name == "Iphone 15"
    assert next(product_iterator).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(product_iterator)
