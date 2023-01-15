from testik import Homes, IncorrectData, NotExistingConf
import pytest
import os


@pytest.mark.xfail(raises=ValueError)
def testvalid1(config='datanotexisting.json'):
    """Test for valid config.

    Args:
        config (str, optional): config of homes. Defaults to 'datanotexisting.json'.
    """
    with open('./maps/{0}'.format(config), 'wt'):
        assert Homes(config)


@pytest.mark.xfail(raises=NotExistingConf)
def testvalid2(config='homes.json'):
    """Test for valid config.

    Args:
        config (str, optional): config of homes. Defaults to 'homes.json'.
    """
    os.remove('./maps/{0}'.format('datanotexisting.json'))
    assert Homes(config)


@pytest.mark.xfail(raises=KeyError)
def testvalid3(config='test_1.json'):
    """Test for valid config.

    Args:
        config (str, optional): config of homes. Defaults to 'test_1.json'.
    """
    assert Homes(config)


@pytest.mark.xfail(raises=Exception)
def testvalid4(config='test_122.json'):
    """Test for valid config.

    Args:
        config (str, optional): config of homes. Defaults to 'test_122.json'.
    """
    assert Homes(config)


@pytest.mark.xfail(raises=ValueError)
def testvalid5(config='tesr.txt.json'):
    """Test for valid config.

    Args:
        config (str, optional): config of homes. Defaults to 'test.txt.json'.
    """
    assert Homes(config)


@pytest.mark.xfail(raises=IncorrectData)
def testdelhome1(choice1=-1, choice2=1):
    """Test for deleting home in conf."""
    assert Homes().delete_home(choice1, choice2)


@pytest.mark.xfail(raises=IncorrectData)
def testdelhome2(choice1=1, choice2=1, expectation=False):
    """Test for deleting home in conf."""
    assert Homes().delete_home(choice1, choice2) == expectation


test_homes = [(2, 1, 1, 1, 1, True), (2, 3, 45, 56, 54, True), (54, 4, 1, 1, 1, False)]


@pytest.mark.xfail(raises=IncorrectData)
@pytest.mark.parametrize('choice1, choice2, height, square, floors, expectation', test_homes)
def testdelhome3(choice1, choice2, height, square, floors, expectation):
    """Test for deleting home in conf.

    Args:
        choice1 (int): first coordinate.
        choice2 (int): second coordinate.
        height (int): height of house.
        square (int): square of house.
        floors (int): number of floors.
        expectation (bool): result of work.
    """
    Homes().add_home(choice1, choice2, height, square, floors)
    assert Homes().delete_home(choice1, choice2) == expectation


@pytest.mark.xfail(raises=IncorrectData)
def testinfo1(choice1=1, choice2=1, expectation=False):
    """Test for inform method.

    Args:
        choice1 (int, optional): first coordinate. Defaults to 1.
        choice2 (int, optional): second coordinate. Defaults to 1.
    """
    assert Homes().inform(choice1, choice2) == expectation


@pytest.mark.xfail(raises=IncorrectData)
def testnewmap2(size1=1, size2=1, name='goodikos.json'):
    """Test for creating new map."""
    assert Homes().new_map(size1, size2, name)
    os.remove('./maps/{0}'.format(name))


harki = [('test007.json', 4, 5, 1, 1, 2, 3, 5, True), ('test008.json', 4, 4, 2, 1, 53, 33, 15, True)]


@pytest.mark.parametrize('name, size1, size2, choice1, choice2, height, square, floors, expectation', harki)
def testaddmethod(name, size1, size2, choice1, choice2, height, square, floors, expectation):
    """Test for adding home in conf.

    Args:
        name (str): name of map.
        size1 (int): first size of map.
        size2 (int): second size of map.
        choice1 (int): first coordinate.
        choice2 (int): second coordinate.
        height (int): height of house.
        square (int): square of house.
        floors (int): number of floors.
    """
    Homes().new_map(size1, size2, name)
    assert Homes(name).add_home(choice1, choice2, height, square, floors) == expectation
    os.remove('./maps/{0}'.format(name))


harki2 = [('test007.json', 4, 5, 1, 1, 'a', 3, 5), ('test008.json', 4, 4, 2, 1, 53, -1, 15)]


@pytest.mark.xfail(raises=IncorrectData)
@pytest.mark.parametrize('name, size1, size2, choice1, choice2, height, square, floors', harki2)
def testaddmethod2(name, size1, size2, choice1, choice2, height, square, floors):
    """Test for adding home in conf.

    Args:
        name (str): name of map.
        size1 (int): first size of map.
        size2 (int): second size of map.
        choice1 (int): first coordinate.
        choice2 (int): second coordinate.
        height (int): height of house.
        square (int): square of house.
        floors (int): number of floors.
    """
    Homes().new_map(size1, size2, name)
    assert Homes(name).add_home(choice1, choice2, height, square, floors)


confs = ['test007.json', 'test008.json']


@pytest.mark.parametrize('conf', confs)
def testdelconf(conf):
    """Delete test confs."""
    os.remove('./maps/{0}'.format(conf))
