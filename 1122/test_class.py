import pytest
from street import House
from setup import SIZE


@pytest.mark.xfail(raises=ValueError)
def xfail_test4():
    """Function must raise ValueError."""
    assert House(SIZE + 1, 0, 1, 1)


@pytest.mark.xfail(raises=ValueError)
def xfail_test0():
    """Function must raise ValueError."""
    assert House(0, SIZE + 1, 1, 1)


@pytest.mark.xfail(raises=ValueError)
def xfail_test1():
    """Function must raise ValueError."""
    assert House(0, 0, 0, 1)


@pytest.mark.xfail(raises=ValueError)
def xfail_test2():
    """Function must raise ValueError."""
    assert House(0, 0, 1, 0)
