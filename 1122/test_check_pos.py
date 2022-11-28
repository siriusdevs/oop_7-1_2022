from setup import SIZE
from functions import check_pos
import pytest


test_num = 12
test_fun_check_pos = [('12', test_num < SIZE), ('0', True), ('r', False)]


@pytest.mark.parametrize('num, res', test_fun_check_pos)
def test_type(num, res):
    """Function checks function for mistakes.

    Args:
        num: str - input number.
        res: bool - expected result.
    """
    assert check_pos(num) == res
