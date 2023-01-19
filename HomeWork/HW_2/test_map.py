"""Testing file."""
import pytest
import map


test_map1 = [('{0}map_brok/'.format(map.Config(title_map="map").PWD), False), (map.Config(title_map="map").PWD, True)]


def ifvalid(pwd):
    """This function valid map.

    Args:
        pwd(str): path to file.json

    Returns:
        bool: yea or bad map.
    """
    try:
        map_city = map.Map.get_cities(pwd)
        if not isinstance(map_city, int):
            if isinstance(map_city.cities, dict):
                map_city.if_valid()
                return True
        return False
    except BaseException:
        return False


@pytest.mark.xfail(raises=map.ImpossibleStructureMap)
@pytest.mark.parametrize('pwd, exception', test_map1)
def test_map(pwd, exception):
    """This test map.

    Args:
        pwd(str): path to file.
        exception(Exception): raise exception
    """
    assert ifvalid(pwd) == exception


test_house = [([5, 5, 10], True), ([3, "3", 4], False), ([-1, 9, 4], False), ([0, 9, 3], None)]


@pytest.mark.xfail(raises=map.ImpossibleHouse)
@pytest.mark.parametrize('arg, exception', test_house)
def test_house_f(arg, exception):
    assert map.House(*arg).if_valid() == exception


test_city = [
    (["Tom", [10, 10]], True),
    (["and", [-1, 4]], False),
    (["Jerry", [None, 4]], None),
    (["Pipe", [9.0, 3]], True)
]


@pytest.mark.xfail(raises=map.ImpossibleCity)
@pytest.mark.parametrize('arg, exception', test_city)
def test_city_f(arg, exception):
    assert map.City(arg[0], arg[1]).if_valid() == exception
