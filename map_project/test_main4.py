"""The tests main4"""
import json
import pytest
from main4 import Building, Map, load_data, save_data


@pytest.fixture
def map():
    return Map(10, 10)


@pytest.mark.parametrize("height, area, floors, x, y", [(5, 100, 2, 5, 5), (6, 150, 3, 6, 6), (7, 200, 4, 7, 7)])
def test_building_init(map, height, area, floors, x, y):
    building = Building(height, area, floors, x, y)
    assert building.height == height
    assert building.area == area
    assert building.floors == floors
    assert building.x == x
    assert building.y == y


def test_map_init(map):
    assert map.x_size == 10
    assert map.y_size == 10
    assert map.buildings == []


@pytest.mark.parametrize("building1, building2", [
    (Building(10, 20, 30, 4, 4), Building(50, 20, 30, 5, 5)),
    (Building(10, 20, 30, 1, 1), Building(60, 20, 30, 2, 2)),
    (Building(10, 20, 30, 3, 3), Building(70, 20, 30, 9, 9)),
])
def test_remove_building(building1, building2, map):
    b1 = building1
    b2 = building2
    map.add_building(b1)
    map.add_building(b2)
    map.remove_building(b1)
    assert map.buildings == [b2]


@pytest.mark.parametrize("building", [
    (Building(5, 100, 2, 5, 5)),
    (Building(6, 150, 3, 6, 6)),
    (Building(5, 100, 2, 5, 5)),
])
def test_map_add_building(building, map):
    b = building
    map.add_building(b)
    assert map.buildings == [b]


def test_save_data(map):
    building1 = Building(5, 100, 2, 5, 5)
    building2 = Building(6, 150, 3, 6, 6)
    map.add_building(building1)
    map.add_building(building2)
    save_data(map.buildings)
    with open("buildings.json", "r") as f:
        data = json.load(f)
    assert data[0]["height"] == 5
    assert data[0]["area"] == 100
    assert data[0]["floors"] == 2
    assert data[0]["x"] == 5
    assert data[0]["y"] == 5
    assert data[1]["height"] == 6
    assert data[1]["area"] == 150
    assert data[1]["floors"] == 3
    assert data[1]["x"] == 6
    assert data[1]["y"] == 6


@pytest.mark.parametrize("building1, building2", [
    (Building(10, 20, 30, 4, 4), Building(50, 20, 30, 5, 5)),
    (Building(10, 20, 30, 1, 1), Building(60, 20, 30, 2, 2)),
    (Building(10, 20, 30, 3, 3), Building(70, 20, 30, 9, 9)),
])
def test_load_data(building1, building2):
    buildings = [building1, building2]
    save_data(buildings)
    loaded_buildings = load_data()
    assert len(loaded_buildings) == 2
    assert loaded_buildings[0].height == building1.height
    assert loaded_buildings[0].area == building1.area
    assert loaded_buildings[0].floors == building1.floors
    assert loaded_buildings[1].height == building2.height
    assert loaded_buildings[1].area == building2.area
    assert loaded_buildings[1].floors == building2.floors