import pytest


def test_lawn_grass_init(test_lawn_grass1):
    assert test_lawn_grass1.name == "Газонная трава"
    assert test_lawn_grass1.description == "Элитная трава для газона"
    assert test_lawn_grass1.price == 500.0
    assert test_lawn_grass1.quantity == 20
    assert test_lawn_grass1.cost == 10000.0
    assert test_lawn_grass1.country == "Россия"
    assert test_lawn_grass1.germination_period == "7 дней"
    assert test_lawn_grass1.color == "Зеленый"


def test_lawn_grass_add(test_lawn_grass1, test_lawn_grass2):
    assert test_lawn_grass1 + test_lawn_grass2 == 16750.0


def test_lawn_grass_add_error(test_lawn_grass1):
    with pytest.raises(TypeError):
        result = test_lawn_grass1 + "трава"  # noqa: F841
