from src.category import Category


def test_category_init(category1, category2):
    assert category1.name == "Смартфоны"
    assert category1.description == "Средство коммуникации"
    assert len(category1.products) == 3

    assert category1.category_count == 2
    assert category2.category_count == 2
    assert Category.category_count == 2

    assert category1.product_count == 4
    assert category2.product_count == 4
    assert Category.product_count == 4
