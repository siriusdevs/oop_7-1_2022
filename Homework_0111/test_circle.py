"""Testing circles_and_triangles. Class Circle."""
from circles_and_triangles import Circle
import pytest


circle_ptrs = [2, 1.8, 3.2, 1]


@pytest.mark.parametrize('radius', circle_ptrs)
def test_circle_ptrs(radius: float) -> None:
    """Test for param of elements of class Circle.

    Args:
        radius: float - radius of a circle
    """
    circle = Circle(radius)
    assert circle.radius == radius


attr_circle = [(2, True), (3, True)]


@pytest.mark.parametrize('radius, res', attr_circle)
def test_attr_circle(radius: float, res: bool) -> None:
    """Test for attributes for an obj of class Circle.

    Args:
        radius: float - radius of a circle.
        res: bool - acceptable attribute or not.
    """
    circle = Circle(radius)
    assert circle.is_valid() == res


circle_area = [(1, 3.142), (1.2, 4.524)]


@pytest.mark.parametrize('radius, area', circle_area)
def test_area_circle(radius: float, area: float) -> None:
    """Test for area of a circle.

    Args:
        radius: float - radius of a circle.
        area: float - area of a circle.
    """
    circle = Circle(radius)
    assert circle.area() == area


circle_len = [(2, 12.566), (1.5, 9.425)]


@pytest.mark.parametrize('radius, len_c', circle_len)
def test_len_circle(radius: float, len_c: float) -> None:
    """Test for len of a circle.

    Args:
        radius: float - radius of a circle.
        len_c: float - len of a circle.
    """
    circle = Circle(radius)
    assert circle.len_of_circle() == len_c
