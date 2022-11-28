import pytest
from street import House
from setup import SIZE


@pytest.mark.xfail(raises=ValueError)
def test_cls_0():
    assert House(SIZE + 1, 0, 1, 1)


@pytest.mark.xfail(raises=ValueError)
def test_cls_1():
    assert House(0, SIZE + 1, 1, 1)


@pytest.mark.xfail(raises=ValueError)
def test_cls_2():
    assert House(0, 0, 0, 1)


@pytest.mark.xfail(raises=ValueError)
def test_cls_3():
    assert House(0, 0, 1, 0)


@pytest.mark.skip()
def test_cls_2():
    assert House(0, 0, 1, 1)
