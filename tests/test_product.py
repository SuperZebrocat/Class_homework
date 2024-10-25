from src.product import Product


def test_product_init(test_product):
    assert test_product.name == "Samsung Galaxy S23 Ultra"
    assert test_product.description == "256GB, Серый цвет, 200MP камера"
    assert test_product.price == 180000.0
    assert test_product.quantity == 5


def test_new_product_classmethod(test_product_dict1, test_product_dict2, test_product_dict3):
    new_product1 = Product.new_product(test_product_dict1)
    assert new_product1.name == "Samsung Galaxy C23 Ultra"
    assert new_product1.description == "256GB, Серый цвет, 200MP камера"
    assert new_product1.price == 180000.0
    assert new_product1.quantity == 5
    assert Product.product_name_list == ["Samsung Galaxy C23 Ultra"]
    assert len(Product.product_list) == 1

    new_product2 = Product.new_product(test_product_dict2)
    assert new_product2.name == "Iphone 15"
    assert Product.product_name_list == ["Samsung Galaxy C23 Ultra", "Iphone 15"]
    assert len(Product.product_list) == 2

    new_product2 = Product.new_product(test_product_dict3)
    assert new_product2.name == "Samsung Galaxy C23 Ultra"
    assert Product.product_name_list == ["Samsung Galaxy C23 Ultra", "Iphone 15"]
    assert len(Product.product_list) == 2
    assert new_product2.quantity == 10
    assert new_product2.price == 180500


def test_price_property(test_product):
    assert test_product.price == 180000


def test_product_price_update(capsys, test_product):
    test_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    test_product.price = -100
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_product_str(test_product):
    assert str(test_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(test_product, test_product2):
    assert test_product + test_product2 == 2580000.0
