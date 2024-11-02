import pytest


def test_smartphone_init(test_smartphone1):
    assert test_smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert test_smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert test_smartphone1.price == 180000.0
    assert test_smartphone1.quantity == 5
    assert test_smartphone1.cost == 900000
    assert test_smartphone1.efficiency == 95.5
    assert test_smartphone1.model == "S23 Ultra"
    assert test_smartphone1.memory == 256
    assert test_smartphone1.color == "Серый"


def test_smartphone_add(test_smartphone1, test_smartphone2):
    assert test_smartphone1 + test_smartphone2 == 2580000.0


def test_smartphone_add_error(test_smartphone1):
    with pytest.raises(TypeError):
        result = test_smartphone1 + 1  # noqa: F841
