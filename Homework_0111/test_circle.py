"""Testing circles_and_triangles. Class Circle."""
from circles_and_triangles import Circle, STerr
import pytest


circle_ptrs = [2, 1.8, 3.2, 1]


@pytest.mark.parametrize('radius', circle_ptrs)
def test_circle_ptrs(radius: float) -> None:
    """Test for param of elements of class Circle.

    Args:
        radius: float - radius of a circle
    """
    assert Circle(radius).radius == radius


@pytest.mark.xfail(raises=STerr)
def test_circle_valid():
    """Tests for circle' STerr."""
    with pytest.raises(STerr):
        Circle(0)

    with pytest.raises(STerr):
        Circle(-3)


attr_circle = [(2, True), (3, True)]


@pytest.mark.parametrize('radius, res', attr_circle)
def test_attr_circle(radius: float, res: bool) -> None:
    """Test for attributes for an obj of class Circle.

    Args:
        radius: float - radius of a circle.
        res: bool - acceptable attribute or not.
    """
    assert Circle(radius).is_valid() == res


circle_area = [(1, 3.142), (1.2, 4.524)]


@pytest.mark.parametrize('radius, area', circle_area)
def test_area_circle(radius: float, area: float) -> None:
    """Test for area of a circle.

    Args:
        radius: float - radius of a circle.
        area: float - area of a circle.
    """
    assert Circle(radius).area() == area


circle_len = [(2, 12.566), (1.5, 9.425)]


@pytest.mark.parametrize('radius, len_c', circle_len)
def test_len_circle(radius: float, len_c: float) -> None:
    """Test for len of a circle.

    Args:
        radius: float - radius of a circle.
        len_c: float - len of a circle.
    """
    assert Circle(radius).len_of_circle() == len_c
