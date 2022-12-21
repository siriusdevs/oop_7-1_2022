import pytest
import sys
sys.path.append('/tests')
from street import street, House
import json

test_write = [((1, 1, 12, 12, 'test_write'), 'test.json', '1', {"<House object>": "(1, 1, 12, 12, 'name')"})]


@pytest.mark.parametrize('par, file_name, action, ans', test_write)
def file_write_check(par, file_name, action, ans):
    """Function which test writing to file.

    Args:
        par: tuple - tuple of parameters for class House.
        file_name: str - name of json file.
        action: str - what function must do.
        ans: dict - dict of classes and parameters for tests.
    """
    street(House(*par), file_name, action)
    with open(file_name, 'r') as map_list:
        street_map = json.load(map_list)
        assert street_map[1] in ans.values()
