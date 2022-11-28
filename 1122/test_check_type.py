import pytest
from functions import check_type


test_fun_check_type = [('12', True), ('0', False), ('r', False)]


@pytest.mark.parametrize('num, res', test_fun_check_type)
def test_type(num, res):
    assert check_type(num) == res

