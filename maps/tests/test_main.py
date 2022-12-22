"""Testing file."""
import pytest
import sys
import os
sys.path.append('..')
from classes import *
test_not_val_building = [(0, 0, 0, False), (1, 'sss', 1, False), (None, None, None, False), (-1, 1, 1, False)]


@pytest.mark.xfail(raises=NotExisting)
@pytest.mark.parametrize('height, base_area, number_of_floors, expectation', test_not_val_building)
def test_not_val_bld(height, base_area, number_of_floors, expectation):
    assert Building(height, base_area, number_of_floors).is_valid() == expectation


test_not_val_map = [(123, 123, 123, False), ("sss", -1, 0, False), ({1: 0}, 1, 1, False), ("Miche", 1, 0, False)]


@pytest.mark.xfail(raises=NotExisting)
@pytest.mark.parametrize('name, width, height, expectation', test_not_val_map)
def test_not_val_mp(name, width, height, expectation):
    assert Map(name, width, height).is_valid() == expectation


test_val_building = [(1, 1, 1, True), (20, 20, 20, True), (20.5, 10.1, 1, True)]


@pytest.mark.parametrize('height, base_area, number_of_floors, expectation', test_val_building)
def test_val_bld(height, base_area, number_of_floors, expectation):
    assert Building(height, base_area, number_of_floors).is_valid() == expectation


test_val_map = [("Miche", 5, 5, True), ("Kirill", 2, 2, True), ("Max2288", 3, 3, True)]


@pytest.mark.parametrize('name, width, height, expectation', test_val_map)
def test_val_mp(name, width, height, expectation):
    assert Map(name, width, height).is_valid() == expectation


test_val_building_dct = [
    (1, 1, 1, {'height': 1, 'base_area': 1, 'number_of_floors': 1}),\
    (20, 20, 20, {'height': 20, 'base_area': 20, 'number_of_floors': 20}),\
    (20.5, 10.1, 1, {'height': 20.5, 'base_area': 10.1, 'number_of_floors': 1})
]


@pytest.mark.parametrize('height, base_area, number_of_floors, expectation', test_val_building_dct)
def test_val_bld_dct(height, base_area, number_of_floors, expectation):
    assert Building(height, base_area, number_of_floors).to_dict() == expectation


test_map_add_bld = [
    ("Miche", 3, 3, 0, 0, 10, 10, 10, ["Miche", 3, 3, 0, 0, 10, 10, 10, ]),
    ("Sochi", 10, 10, 1, 1, 7, 7, 7, ["Sochi", 10, 10, 1, 1, 7, 7, 7]),
    ("Albinos", 100, 100, 50, 50, 3, 3, 3, ["Albinos", 100, 100, 50, 50, 3, 3, 3])
]


@pytest.mark.parametrize('name, width, height, x_coordinate, y_coordinate, \
    height_bld, base_area, number_of_floors, expectation', test_map_add_bld
                         )
def test_add_bld(name, width, height, x_coordinate, y_coordinate, height_bld, base_area, number_of_floors, expectation):
    miche = Map(name, width, height)
    miche.add_map_to_json()
    miche.add_building(x_coordinate, y_coordinate, Building(height_bld, base_area, number_of_floors))
    with open("maps.json", 'rt') as file_json:
        data_to_open = json.load(file_json)
    lst_to_assert = []
    lst_to_assert.append(list(data_to_open["maps"][0].keys())[0])
    lst_to_assert.append(data_to_open["maps"][0]["width"])
    lst_to_assert.append(data_to_open["maps"][0]["height"])
    for el in data_to_open["maps"][0]["buildings"]:
        if not el:
            continue
        lst_to_assert.append(el[0])
        lst_to_assert.append(el[1])
        lst_to_assert.append(el[2]["height"])
        lst_to_assert.append(el[2]["base_area"])
        lst_to_assert.append(el[2]["number_of_floors"])
    assert lst_to_assert == expectation
    os.remove("maps.json")


test_map_del_bld = [
    ("Miche", 3, 3, 0, 0, 10, 10, 10, ["Miche", 3, 3, 0]),
    ("Sochi", 10, 10, 1, 1, 7, 7, 7, ["Sochi", 10, 10, 0]),
    ("Albinos", 100, 100, 50, 50, 3, 3, 3, ["Albinos", 100, 100, 0])
]


@pytest.mark.parametrize('name, width, height, x_coordinate, y_coordinate, height_bld, base_area, number_of_floors, expectation', test_map_del_bld)
def test_del_bld(name, width, height, x_coordinate, y_coordinate, height_bld, base_area, number_of_floors, expectation):
    miche = Map(name, width, height)
    miche.add_map_to_json()
    miche.add_building(x_coordinate, y_coordinate, Building(height_bld, base_area, number_of_floors))
    miche.delete_building(x_coordinate, y_coordinate)
    with open("maps.json", 'rt') as file_json:
        data_to_open = json.load(file_json)
    lst_to_assert = []
    lst_to_assert.append(list(data_to_open["maps"][0].keys())[0])
    lst_to_assert.append(data_to_open["maps"][0]["width"])
    lst_to_assert.append(data_to_open["maps"][0]["height"])
    lst_to_assert.append(len(data_to_open["maps"][0]["buildings"]))
    assert lst_to_assert == expectation
    os.remove("maps.json")
