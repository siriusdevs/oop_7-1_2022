import pytest
from street import street, House
import json

test_write = [((1, 1, 12, 12, 'test_write'), 'test.json', '1', {"<street.House object at 0x7f671d32ff10>": "(1, 1, 12, 12, 'name')"})]


@pytest.mark.parametrize('parameters, file_name, action, result', test_write)
def file_write_check(parameters, file_name, action, result):
    street(House(*parameters, file_name, action))
    with open(file_name, 'r') as map_list:
        street_map = json.load(map_list)
        assert street_map == result
        