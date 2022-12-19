"""Tests for classes of Building and Map."""
from building_map import Building, Map, InvalidAttribute
import conf_test
import pytest

# Tests for Building


def test_str_attr_building():
    """Test string attribute."""
    with pytest.raises(InvalidAttribute):
        Building('height', 3, 6)


def test_negative_attr_building():
    """Test negative attribute."""
    with pytest.raises(InvalidAttribute):
        Building(3, 9, -10)


def test_zero_attr_building():
    """Test zero attribute."""
    with pytest.raises(InvalidAttribute):
        Building(3, 9, 0)


tests_building_init = [
    (50, 10, 12, (1, 5)),
    (10, 5, 5, (3, 4)),
    (150, 50, 18, (2, 8))
]


@pytest.mark.parametrize('height, area, floors, location', tests_building_init)
def test_init_building(height: int, area: int, floors: int, location: tuple) -> None:
    """Test building's initialization."""
    building = Building(height, area, floors, location)
    assert building.height == height
    assert building.area == area
    assert building.floors == floors
    assert building.location == location


tests_b_methods = [
    (conf_test.BUILD1['obj'], conf_test.BUILD1['dict']),
    (conf_test.BUILD2['obj'], conf_test.BUILD2['dict']),
    (conf_test.BUILD3['obj'], conf_test.BUILD3['dict'])
]


@pytest.mark.parametrize('given_data, output', tests_b_methods)
def test_to_dict_building(given_data: Building, output: dict) -> None:
    """Test method to_dict."""
    assert given_data.to_dict() == output


@pytest.mark.parametrize('output, given_data', tests_b_methods)
def test_from_dict_building(given_data: dict, output: Building) -> None:
    """Test method from_dict."""
    new_build = Building.from_dict(**given_data)
    assert new_build.height == output.height
    assert new_build.area == output.area
    assert new_build.floors == output.floors
    assert new_build.location == output.location


tests_str_method_b = [
    (conf_test.BUILD1['obj'], conf_test.BUILD1['str']),
    (conf_test.BUILD2['obj'], conf_test.BUILD2['str']),
    (conf_test.BUILD3['obj'], conf_test.BUILD3['str'])
]


@pytest.mark.parametrize('given_data, output', tests_str_method_b)
def test_str_method(given_data: Building, output: str) -> None:
    """Test __str__ method."""
    assert str(given_data) == output


# Tests for Map

def test_str_attr_map():
    """Test string attribute."""
    with pytest.raises(InvalidAttribute):
        Map('length', 4)


def test_negative_attr_map():
    """Test negative attribute."""
    with pytest.raises(InvalidAttribute):
        Map(3, -10)


def test_zero_attr_map():
    """Test zero attribute."""
    with pytest.raises(InvalidAttribute):
        Map(3, 0)


tests_map_init = [
    (4, 6, conf_test.MAP1_A['builds']),
    (10, 5, conf_test.MAP2_A['builds']),
    (7, 3, conf_test.MAP3_A['builds'])
]


@pytest.mark.parametrize('length, width, buildings', tests_map_init)
def test_init_map(length: int, width: int, buildings: dict) -> None:
    """Test building's initialization."""
    map_ = Map(length, width, buildings)
    assert map_.length == length
    assert map_.width == width
    assert map_.buildings == buildings


tests_m_methods = [
    (conf_test.MAP1['obj'], conf_test.MAP1['dict']),
    (conf_test.MAP2['obj'], conf_test.MAP2['dict']),
    (conf_test.MAP3['obj'], conf_test.MAP3['dict'])
]


@pytest.mark.parametrize('given_data, output', tests_m_methods)
def test_to_dict_map(given_data: Map, output: dict) -> None:
    """Test method to_dict."""
    assert given_data.to_dict() == output


@pytest.mark.parametrize('output, given_data', tests_m_methods)
def test_from_dict_map(given_data: dict, output: Map) -> None:
    """Test method from_dict."""
    new_map = Map.from_dict(**given_data)
    assert new_map.length == output.length
    assert new_map.width == output.width
    assert new_map.buildings == output.buildings


tests_str_method_m = [
    (conf_test.MAP1['obj'], conf_test.MAP1['str']),
    (conf_test.MAP2['obj'], conf_test.MAP2['str']),
    (conf_test.MAP3['obj'], conf_test.MAP3['str'])
]


@pytest.mark.parametrize('given_data, output', tests_str_method_m)
def test_str_method_map(given_data: Map, output: str) -> None:
    """Test __str__ method."""
    assert str(given_data) == output
