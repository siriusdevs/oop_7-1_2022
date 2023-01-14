"""Testing file for maps."""
import pytest

from model.buildings import BasicBuilding
from model.exeptions import CardError
from model.maps import BasicMap


def test_create_map_from_dict():
    """Tests for create a map from dict."""
    dictionary = {"name": "Test", "width": 10, "height": 10, "building_field_by_name": True, "builds": []}
    card = BasicMap.from_dict(dictionary)
    assert card.name == dictionary["name"]


@pytest.mark.xfail(raises=CardError)
def test_create_map_from_dict_not_val():
    """Tests for create a map from not valid dict."""
    dictionary = {"width": 10, "height": 10, "building_field_by_name": True, "builds": []}
    with pytest.raises(CardError):
        BasicMap.from_dict(dictionary)


def test_to_dict_val():
    """Tests for generate maps' dict."""
    dictionary = {"name": "Test", "width": 10, "height": 10, "building_field_by_name": True, "builds": []}
    card = BasicMap(dictionary["name"], dictionary["width"], dictionary["height"])
    assert card.to_dict() == dictionary


def test_add_building():
    """Tests for add building to map."""
    dictionary = {"name": "Test", "width": 10, "height": 10, "building_field_by_name": True, "builds": []}
    card = BasicMap(dictionary["name"], dictionary["width"], dictionary["height"])
    building = BasicBuilding("Building 1", 100.1, 1, 100.0)
    card.add_building(0, 0, building)
    assert card.get_info(0, 0) == str(building)


def test_get_info_empty():
    """Tests for get info about empty field."""
    dictionary = {"name": "Test", "width": 10, "height": 10, "building_field_by_name": True, "builds": []}
    card = BasicMap(dictionary["name"], dictionary["width"], dictionary["height"])
    building = BasicBuilding("Building 1", 100.1, 1, 100.0)
    card.add_building(0, 0, building)
    assert card.get_info(1, 1) == "Empty field"


@pytest.mark.xfail(raises=CardError)
def test_get_info_wrong_pos():
    """Tests for get info about wrong position."""
    dictionary = {"name": "Test", "width": 10, "height": 10, "building_field_by_name": True, "builds": []}
    card = BasicMap(dictionary["name"], dictionary["width"], dictionary["height"])
    with pytest.raises(CardError):
        card.get_info(0, 100)


def test_del_building():
    """Tests for del building from map."""
    dictionary = {"name": "Test", "width": 10, "height": 10, "building_field_by_name": True, "builds": []}
    card = BasicMap(dictionary["name"], dictionary["width"], dictionary["height"])
    building = BasicBuilding("Building 1", 100.1, 1, 100.0)
    card.add_building(0, 0, building)
    assert card.get_info(0, 0) == str(building)
    card.del_by_pos(0, 0)
    assert card.get_info(0, 0) == "Empty field"
