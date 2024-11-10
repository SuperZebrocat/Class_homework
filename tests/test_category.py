import pytest

from src.category import Category


def test_category_init(test_category1, test_category2):
    assert test_category1.name == "Смартфоны"
    assert test_category1.description == "Средство коммуникации"
    assert len(test_category1.products_in_list) == 3

    assert test_category1.category_count == 2
    assert test_category2.category_count == 2
    assert Category.category_count == 2

    assert test_category1.product_count == 4
    assert test_category2.product_count == 4
    assert Category.product_count == 4


def test_add_product(test_category1, test_product):
    test_category1.add_product(test_product)
    assert test_category1.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\nIphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
    )


def test_products_property(test_category1):
    assert test_category1.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\nXiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_products_in_list_property(test_category1, test_product):
    assert len(test_category1.products_in_list) == 3
    test_category1.add_product(test_product)
    assert len(test_category1.products_in_list) == 4


def test_category_str(test_category1):
    assert str(test_category1) == "Смартфоны, количество продуктов: 27 шт."


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(product_iterator).name == "Iphone 15"
    assert next(product_iterator).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(product_iterator)


def test_add_product_error(test_category1):
    with pytest.raises(TypeError):
        test_category1.add_product("not a product")


def test_add_product_smartphone(test_category1, test_smartphone1):
    test_category1.add_product(test_smartphone1)
    assert test_category1.products_in_list[-1].name == "Samsung Galaxy S23 Ultra"


def test_middle_price(test_category1, test_category_empty):
    assert test_category1.middle_price() == 140333.33
    assert test_category_empty.middle_price() == 0
