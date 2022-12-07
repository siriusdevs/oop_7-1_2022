"""Testing buildWorker.py."""
import buildWorker
import pytest
from time import sleep
from json import load 

building_ptrs = [('Hello', 7, 6, 1, 2, 3), ('Second', 1.8, 3.2, 4, 1, 3)]


@pytest.mark.parametrize('name, height, width, floors, coord_x, coord_y', building_ptrs)
def test_building_ptrs(name, height, width, floors, coord_x, coord_y) -> None:
    """Test for param of elements of class Building.

    Args:
        name: str - name of a building.
        height: float - height of a building.
        width: float - width of a building.
        floors: int - number of floors of a building.
        coord_x: int - coordinate x of a building on the map.
        coord_y: int - coordinate y of a building on the map.
    """
    assert buildWorker.Building(name, height, width, floors, coord_x, coord_y).name == name
    assert buildWorker.Building(name, height, width, floors, coord_x, coord_y).height == height
    assert buildWorker.Building(name, height, width, floors, coord_x, coord_y).width == width
    assert buildWorker.Building(name, height, width, floors, coord_x, coord_y).floors == floors
    assert buildWorker.Building(name, height, width, floors, coord_x, coord_y).coord_x == coord_x
    assert buildWorker.Building(name, height, width, floors, coord_x, coord_y).coord_y == coord_y


@pytest.mark.xfail(raises=buildWorker.BuildErr)
def test_building_valid():
    """Tests for buildings' BuildErr."""
    with pytest.raises(buildWorker.BuildErr):
        assert buildWorker.Building(4, 1, 3, -1, 3, 0)
    with pytest.raises(buildWorker.BuildErr):
        assert buildWorker.Building('Hi', 1, 3, -1, 3, 0)
    with pytest.raises(buildWorker.BuildErr):
        assert buildWorker.Building('Hi', -1, -3, 1, 3, 3)


map_ptrs = [(2, 3), (1, 4)]


@pytest.mark.parametrize('length, width', map_ptrs)
def test_map_ptrs(length, width) -> None:
    """Test for param of elements of class Map.

    Args:
        length: int - length of a map.
        width: int - width of a map.
    """
    assert buildWorker.Map(length, width).length == length
    assert buildWorker.Map(length, width).width == width


@pytest.mark.xfail(raises=buildWorker.MapErr)
def test_map_valid():
    """Tests for maps' MapErr."""
    with pytest.raises(buildWorker.MapErr):
        assert buildWorker.Map(4, -1)
    with pytest.raises(buildWorker.MapErr):
        assert buildWorker.Map(0, 7)
    with pytest.raises(buildWorker.MapErr):
        assert buildWorker.Map(-2, 0)


def test_maps() -> None:
    """Test for maps."""
    for hi in buildWorker.Town.maps():
        assert isinstance(hi[0], str)


def test_see_map() -> None:
    """Test for see_map."""
    for hi in buildWorker.Town.see_map('{}.json'.format(buildWorker.Town.maps()[0][0])):
        for ih in hi:
            assert ih == 0 or ih == 'X'


@pytest.mark.xfail(raises=Exception)
def test_see_map_r() -> None:
    """Test for see_map."""
    for hi in buildWorker.Town.see_map('town3(town_for_tests).json'):
        for ih in hi:
            assert ih == 0 or ih == 'X'


see_build_prts = [('22', {
    "name": "School",
    "Floors": 4
}), ('23', 'No such a building')]


@pytest.mark.parametrize('coordinates, information', see_build_prts)
def test_see_build_ptrs(coordinates, information) -> None:
    """Test for see_buildings.

    Args:
        information - result of a funtion.
        coordinates: str - building\'s coordinates on the map.
    """
    file_name = 'town3(town_for_tests).json'
    assert buildWorker.Town.see_buildings(file_name, coordinates) == information

add_building_prts = [buildWorker.Building('Max', 1, 1, 1, 1, 1), buildWorker.Building('Kirill', 1, 1, 1, 3, 3)]

@pytest.mark.parametrize('building', add_building_prts)
def test_add_building(building) -> None:
    """Test for add_building.

    Args:
        building - building for addition.
    """
    file_name = 'town3(town_for_tests).json'
    buildWorker.Town.add_building(file_name, building)
    coordinates = str(building.coord_y) + str(building.coord_x)
    with open(file_name, 'rt') as json_file:
            inf = load(json_file)
    assert coordinates in inf
    buildWorker.Town.destroy_building(file_name, coordinates)
    with open(file_name, 'rt') as json_file:
            inf = load(json_file)
    assert not (coordinates in inf)
