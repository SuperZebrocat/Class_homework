from src.utils import create_objects_from_json


def test_create_objects_from_json(json_data):
    categories = create_objects_from_json(json_data)
    assert categories[0].name == "Смартфоны"
    assert categories[1].name == "Телевизоры"
