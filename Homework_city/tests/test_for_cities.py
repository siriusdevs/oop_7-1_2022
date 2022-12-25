"""File for tests cities."""
from typing import List
import pytest

from Homework_city.classes import City, House
from Homework_city.exceptions import DoesntExistParamsOnMap, MapFileDoesntExist, InvalidConfigurationsMap, \
    InvalidMapSize, InvalidValuesInParamsBuilding, InvalidBuildingParams, InvalidCountOfBuildings, InvalidRowOrCol, \
    NullHouseError, HouseInsertToHouse
from contextlib import nullcontext as does_not_raise

path_1 = "maps_for_test/test_map_1.json"


@pytest.mark.xfail(raises=DoesntExistParamsOnMap())
def tests_for_doesnt_exist_param_in_map() -> None:
    """Test of reading the error of finding the main keys of the map."""
    with pytest.raises(DoesntExistParamsOnMap):
        City(path_1)


@pytest.mark.xfail(raises=MapFileDoesntExist())
def tests_for_doesnt_exist_map() -> None:
    """Transfer tests for a non-existent map."""
    with pytest.raises(MapFileDoesntExist):
        City("12233_map.json")


path_2 = "maps_for_test/test_map_2.json"


@pytest.mark.xfail(raises=InvalidConfigurationsMap())
def tests_for_map_with_inv_vals_conf_params() -> None:
    """Test for a card with incorrect parameters."""
    with pytest.raises(InvalidConfigurationsMap):
        City(path_2)


path_3 = "maps_for_test/test_map_3.json"


@pytest.mark.xfail(raises=InvalidMapSize())
def tests_for_map_with_inv_size() -> None:
    """Test for card with incorrect size."""
    with pytest.raises(InvalidMapSize):
        City(path_3)


path_4 = "maps_for_test/test_map_4.json"


@pytest.mark.xfail(raises=InvalidValuesInParamsBuilding())
def tests_for_map_with_inv_house_values() -> None:
    """Test for a map with incorrect building values."""
    with pytest.raises(InvalidValuesInParamsBuilding):
        City(path_4)


path_5 = "maps_for_test/test_map_5.json"


@pytest.mark.xfail(raises=InvalidBuildingParams())
def tests_for_map_with_inv_house_params() -> None:
    """Test for a map with incorrect building keys."""
    with pytest.raises(InvalidBuildingParams):
        City(path_5)


path_6 = "maps_for_test/test_map_6.json"


@pytest.mark.xfail(raises=InvalidCountOfBuildings())
def tests_for_map_with_inv_count_houses() -> None:
    """Test for a map with the wrong number of houses."""
    with pytest.raises(InvalidCountOfBuildings):
        City(path_6)


paths_valid_files = [("maps_for_test/small_file.json", does_not_raise()),
                     ("maps_for_test/big_file.json", does_not_raise()),
                     ("maps_for_test/empty_file.json", does_not_raise())]


@pytest.mark.parametrize('path, expectation', paths_valid_files)
def tests_not_raises_for_read_files(path: str, expectation: object) -> None:
    """
    Various map reading test.
    Args:
        path: str - path to file.
        expectation: object - expected result.
    """
    with expectation:
        assert City(path) is not None


paths_valid_files = [("maps_for_test/small_file_copy.json", does_not_raise()),
                     ("maps_for_test/big_file_copy.json", does_not_raise()),
                     ("maps_for_test/empty_file_copy.json", does_not_raise())]


@pytest.mark.parametrize('path, expectation', paths_valid_files)
def tests_not_raises_for_save_files(path: str, expectation: object) -> None:
    """
    Test writing and then reading cards.
    Args:
        path: str - path to file.
        expectation: object - expected result.
    """
    City(path).save_map()
    with expectation:
        assert City(path) is not None


vals_for_test_print = [("maps_for_test/test_map_0.json", "⌂  ×\n×  ×")]


@pytest.mark.parametrize('path, result', vals_for_test_print)
def tests_print_map(path: str, result: str) -> None:
    """
    Map output function test.
    Args:
        path: str - path to file.
        result: str - correct method output.
    """
    assert City(path).print_map() == result


vals_test_rows_and_cols = [(1, 1, does_not_raise()), (0, 1, does_not_raise()), (2, 1, pytest.raises(InvalidRowOrCol))]


@pytest.mark.parametrize('row, col, expectation', vals_test_rows_and_cols)
def tests_valid_row_and_col(row: int, col: int, expectation: object) -> None:
    """
    Test to check rows and columns for map.
    Args:
        row: int - row.
        col: int - column.
        expectation: object - expected result.
    """
    with expectation:
        assert City("maps_for_test/test_map_0.json").validation_rows_and_cols(row, col) is not None


val_test_get_house = [(0, 0, ["A", 20, 30, 50])]


@pytest.mark.parametrize('row, col, res', val_test_get_house)
def test_get_house(row: int, col: int, res: List) -> None:
    """
    Test for checking a function that returns a house from a map.
    Args:
        row: int - row.
        col: int - colum.
        res: valid params for house.
    """
    assert City("maps_for_test/test_map_0.json").get_house(row, col).params == res


@pytest.mark.xfail(raises=NullHouseError())
def test_get_err_house() -> None:
    """Test for checking a function that returns a non-existent house from the map."""
    with pytest.raises(NullHouseError):
        City("maps_for_test/test_map_0.json").get_house(1, 1)


val_for_set_house = [(1, 1, House("test", 20, 50, 2), ["test", 20, 50, 2])]


@pytest.mark.parametrize("row, col, house, expected_params", val_for_set_house)
def test_set_house_to_map(row: int, col: int, house: House, expected_params: List) -> None:
    """
    Test adding a house to the map.
    Args:
        row: int - row
        col: int - colum
        house: House - the house that we add to the map
        expected_params: home parameters that the previously tested method should return get_house
    """
    test_city = City("maps_for_test/test_map_7.json")
    test_city.set_house(row, col, house)
    test_house = test_city.get_house(row, col).params
    test_city.del_house(row, col)
    assert test_house == expected_params


@pytest.mark.xfail(raises=HouseInsertToHouse())
def test_err_set_house_to_map() -> None:
    """Test for adding a house by those coordinates that already have a house."""
    with pytest.raises(HouseInsertToHouse):
        City("maps_for_test/test_map_0.json").set_house(0, 0, House("test", 20, 50, 2))
