"""This file for tests houses."""
from typing import List
import pytest
from classes import House
from exceptions import NothingToChange, InvalidHouseParams, NullHouseParams, InvalidHouseName

tests_create_houses = [(["one", 20, 50, 2]), (["two", 40, 100, 4]), (["three", 15, 25, 1])]


@pytest.mark.parametrize('params_h', tests_create_houses)
def test_house_create(params_h: List) -> None:
    """
    Home creation test.
    Args:
        params_h: List of house params.
    """
    house = House(*params_h)
    assert house.par_h == params_h


test_change_house = [(House("one", 20, 50, 2), ["new", 40, 50, 2])]


@pytest.mark.parametrize("house, expect", test_change_house)
def test_to_change_house(house: House, expect: List) -> None:
    """
    Home change test.
    Args:
        house: object of class House.
        expect: expected result.
    """
    house.change_params(name="new", height=40)
    assert house.par_h == expect


test_for_home_str = [(House("one", 20, 50, 2), "Params for this house:\n\
1. name: one\n2. height: 20\n3. base area: 50\n4. number of floors: 2")]


@pytest.mark.parametrize("house, expect", test_for_home_str)
def test_for_house_str(house: House, expect: str) -> None:
    """
    Home parameter output test.
    Args:
        house: object of class House.
        expect: expected result.
    """
    assert str(house) == expect


@pytest.mark.xfail(raises=NothingToChange())
def test_err_change_house():
    """Test for calling an error NothingToChange."""
    with pytest.raises(NothingToChange):
        House("one", 20, 50, 2).change_params()


@pytest.mark.xfail(raises=InvalidHouseParams())
def test_err_create_house_with_none_int_param():
    """Home creation test with incorrect parameters."""
    with pytest.raises(InvalidHouseParams):
        House("one", "20", 50, 2)


@pytest.mark.xfail(raises=NullHouseParams())
def test_err_create_house_with_null_param():
    """Test for creating a house with zero parameters."""
    with pytest.raises(NullHouseParams):
        House("one", 20, 50, 0)


@pytest.mark.xfail(raises=InvalidHouseName())
def test_err_create_house_with_invalid_name():
    """Test for creating a house with the wrong name."""
    with pytest.raises(InvalidHouseName):
        House("", 20, 50, 2)

    with pytest.raises(InvalidHouseName):
        House(12, 20, 50, 2)

    with pytest.raises(InvalidHouseName):
        House(12.3, 20, 50, 2)
