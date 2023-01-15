"""The tests main3"""

import pytest
from main3 import Building, Map, load_data, save_data
import json


@pytest.mark.parametrize("x, y, z, expected_result", [
    (10, 20, 30, Building(10, 20, 30)),
    (1, 5, 1, Building(1, 5, 1)),
    (1000, 2000, 100, Building(1000, 2000, 100)),
])
def test_building_init(x, y, z, expected_result):
    b = Building(x, y, z)
    assert b.height == expected_result.height
    assert b.area == expected_result.area
    assert b.floors == expected_result.floors


@pytest.mark.parametrize("x, expected_result", [
    (10, Map(10)),
    (20, Map(20)),
    (30, Map(30)),
])
def test_map_init(x, expected_result):
    m = Map(x)
    assert m.size == expected_result.size
    assert m.buildings == []


@pytest.mark.parametrize("x, building", [
    (10, Building(10, 20, 30)),
    (20, Building(10, 20, 30)),
    (30, Building(10, 20, 30)),
])
def test_add_building(x, building):
    m = Map(x)
    b = building
    m.add_building(b)
    assert m.buildings == [b]


@pytest.mark.parametrize("x, building1, building2", [
    (10, Building(10, 20, 30), Building(50, 20, 30)),
    (20, Building(10, 20, 30), Building(60, 20, 30)),
    (30, Building(10, 20, 30), Building(70, 20, 30)),
])
def test_remove_building(x, building1, building2):
    m = Map(x)
    b1 = building1
    b2 = building2
    m.add_building(b1)
    m.add_building(b2)
    m.remove_building(b1)
    assert m.buildings == [b2]


@pytest.mark.parametrize("building1, building2", [
    (Building(10, 20, 30), Building(50, 20, 30)),
    (Building(10, 20, 30), Building(60, 20, 30)),
    (Building(10, 20, 30), Building(70, 20, 30)),
])
def test_save_data(building1, building2):
    buildings = [building1, building2]
    save_data(buildings)
    with open("buildings.json", "r") as f:
        data = json.load(f)
    assert data == [{"height": building1.height, "area": building1.area, "floors": building1.floors}, {"height": building2.height, "area": building2.area, "floors": building2.floors}]


@pytest.mark.parametrize("building1, building2", [
    (Building(10, 20, 30), Building(50, 20, 30)),
    (Building(10, 20, 30), Building(60, 20, 30)),
    (Building(10, 20, 30), Building(70, 20, 30)),
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