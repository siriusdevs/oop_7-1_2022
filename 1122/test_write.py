import pytest
from street import street, House, for_remove
from functions import inp_json
import os

test_write = [((1, 1, 12, 12, 'test_write'), 'test.json', '1', {"<House object>": "(1, 1, 12, 12, 'test_write')"})]
test_replace = [((1, 1, 200, 200, 'test_replace'), 'test.json', '1', None)]
test_remove = [((1, 1, 200, 200, 'test_move'), 'test.json', '2', [])]


def from_obj(cls_obj):
    """Function which must divide class object on parameters.

    Args:
        cls_obj: House - class object of house.

    Returns:
        tuple - tuple with all parameters of house.
    """
    return (cls_obj.x_pos, cls_obj.y_pos, cls_obj.square, cls_obj.height, cls_obj.name)


@pytest.mark.parametrize('par, file_name, action, ans', test_write)
def test_file_write1(par, file_name, action, ans):
    """Function which test writing to file.

    Args:
        par: tuple - tuple of parameters for class House.
        file_name: str - name of json file.
        action: str - what function must do.
        ans: dict - dict of classes and parameters for tests.
    """
    street(House(*par), file_name, action)
    street_map = inp_json(file_name)
    assert str(from_obj(street_map[0])) in ans.values()


@pytest.mark.parametrize('par, file_name, action, ans', test_remove)
def test_file_remove(par, file_name, action, ans):
    """Function which test writing to file.

    Args:
        par: tuple - tuple of parameters for class House.
        file_name: str - name of json file.
        action: str - what function must do.
        ans: dict - dict of classes and parameters for tests.
    """
    assert for_remove(file_name, House(*par)) == ans


@pytest.mark.parametrize('par, file_name, action, ans', test_write)
def test_file_write2(par, file_name, action, ans):
    """Function which test writing to file.

    Args:
        par: tuple - tuple of parameters for class House.
        file_name: str - name of json file.
        action: str - what function must do.
        ans: dict - dict of classes and parameters for tests.
    """
    street(House(*par), file_name, action)
    street_map = inp_json(file_name)
    assert str(from_obj(street_map[0])) in ans.values()


@pytest.mark.parametrize('par, file_name, action, ans', test_replace)
def test_file_replace(par, file_name, action, ans):
    """Function which test writing to file.

    Args:
        par: tuple - tuple of parameters for class House.
        file_name: str - name of json file.
        action: str - what function must do.
        ans: dict - dict of classes and parameters for tests.
    """
    assert street(House(*par), file_name, action) is ans
    os.remove(file_name)
