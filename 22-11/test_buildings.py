"""Testing file for buildings."""
import pytest

from model.buildings import BasicBuilding
from model.exeptions import BuildingError

test_val_buildings = [("Building 1", 100.1, 1, 100.0),
                      ("Building 2", 200.2, 2, 100.0),
                      ("Building 3", 300.3, 3, 100.0)]


@pytest.mark.parametrize('name, height, floor, area', test_val_buildings)
def test_building_create(name: str, height: float, floor: int, area: float) -> None:
    """Test for create buildings.

    Args:
        name: str -  name of the building.
        height: float -  height of the building.
        floor: int - floor of the building.
        area: float - area of the building.
    """
    building = BasicBuilding(name, height, floor, area)
    assert building.name == name
    assert building.height == height
    assert building.floor == floor
    assert building.area == area


@pytest.mark.xfail(raises=BuildingError)
def test_err_invalid_buildings1():
    """Tests for buildings' BuildingError."""
    with pytest.raises(BuildingError):
        BasicBuilding("Test1", -10, 100, 200)

    with pytest.raises(BuildingError):
        BasicBuilding("Test2", 10, -100, 200)

    with pytest.raises(BuildingError):
        BasicBuilding("Test3", 10, 100, -200)


@pytest.mark.xfail(raises=ValueError)
def test_err_invalid_buildings2():
    """Tests for buildings' ValueError."""
    with pytest.raises(ValueError):
        BasicBuilding("Test1", "3131", 100, 200)

    with pytest.raises(ValueError):
        BasicBuilding("Test2", 10, "dsa", 200)

    with pytest.raises(ValueError):
        BasicBuilding("Test3", 10, 100, "fdscadf")


def test_from_dict_val():
    """Tests for create buildings from dict."""
    dictionary = {"name": "Test1", "height": 100.0, "floor": 10, "area": 200.0}
    building = BasicBuilding.create_build_from_dict(dictionary)
    assert building.name == dictionary["name"]


@pytest.mark.xfail(raises=BuildingError)
def test_from_dict_not_val():
    """Tests for create buildings from not valid dict."""
    dictionary = {"height": 100.0, "floor": 10, "area": 200.0}
    with pytest.raises(BuildingError):
        BasicBuilding.create_build_from_dict(dictionary)


def test_to_dict_val():
    """Tests for generate buildings' dict."""
    dictionary = {"name": "Test1", "height": 100, "floor": 10, "area": 200}
    building = BasicBuilding(dictionary["name"],
                             dictionary["height"],
                             dictionary["floor"],
                             dictionary["area"])
    assert building.to_dict() == dictionary
