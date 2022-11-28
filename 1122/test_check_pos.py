from setup import SIZE
from functions import check_pos
import pytest


test_fun_check_pos = [('12', 12 < SIZE), ('0', True), ('r', False)]


@pytest.mark.parametrize('num, res', test_fun_check_pos)
def test_type(num, res):
    assert check_pos(num) == res
