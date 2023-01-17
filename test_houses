import pytest
from houses import Building


@pytest.mark.xfail(raises=ValueError)
def test0():
    """Function must raise ValueError."""
    assert Building(0, 0, 0, 1)


@pytest.mark.xfail(raises=ValueError)
def test1():
    """Function must raise ValueError."""
    assert Building(0, 0, 0, -1)


@pytest.mark.xfail(raises=ValueError)
def test2():
    """Function must raise ValueError."""
    assert Building(0, 0, 0, 0)


@pytest.mark.xfail(raises=ValueError)
def test3():
    """Function must raise ValueError."""
    assert Building(1, 0, -100, 51)
