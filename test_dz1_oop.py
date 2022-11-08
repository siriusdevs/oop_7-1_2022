"""Testing file."""
import pytest
from dz1_oop import Circle, Triangle

test_triangle_parametrs = [(1, 2, 3)]


@pytest.mark.parametrize('side1, side2, side3', test_triangle_parametrs)
def test_triangle(side1: int, side2: int, side3: int) -> None:
    """Test for it.
    Args:
        side1 (float): first side of triangle.
        side2 (float): second side of triangle.
        side3 (float): third side of triangle.
    """
    triangle = Triangle(side1, side2, side3)
    assert triangle.side1 == side1
    assert triangle.side2 == side2
    assert triangle.side3 == side3


test_circle_parametrs = [(1), (2), (3)]


@pytest.mark.parametrize('radius', test_circle_parametrs)
def test_circle(radius: int) -> None:
    """Test for it.
    Args:
        radius (int): circle's radius.
    """
    circle = Circle(radius)
    assert circle.r == radius


test_triangle_perimeter = [(1, 2, 3, 6)]


@pytest.mark.parametrize('side1, side2, side3, expect', test_triangle_perimeter)
def test_perimeter(side1: int, side2: int, side3: int, expect: int) -> None:
    """Test for it.
    Args:
        side1 (float): first side of triangle.
        side2 (float): second side of triangle.
        side3 (float): third side of triangle.
        expect (float): triangle's perimeter.
    """
    triangle = Triangle(side1, side2, side3)
    assert triangle.p_() == expect


test_triangle_square = [(3, 4, 5, 77.77)]


@pytest.mark.parametrize('side1, side2, side3, expect', test_triangle_square)
def test_square(side1: int, side2: int, side3: int, expect: float) -> None:
    """Test for it.
    Args:
        side1 (float): first side of triangle.
        side2 (float): second side of triangle.
        side3 (float): third side of triangle.
        expect (float): triangle's square.
    """
    triangle = Triangle(side1, side2, side3)
    assert triangle.s_() == expect


test_circle_length = [(2, 12.57)]


@pytest.mark.parametrize('radius, expect', test_circle_length)
def test_length(radius: int, expect: float) -> None:
    """Test for it.
    Args:
        radius (float): circle's radius.
        expect (float): circle's length.
    """
    circle = Circle(radius)
    assert circle.l_() == expect


test_circle_square = [(3, 28.27)]


@pytest.mark.parametrize('radius, expect', test_circle_square)
def test_c_square(radius: int, expect: float) -> None:
    """Test for it.
    Args:
        radius (float): circle's radius.
        expect (float): circle's length.
    """
    circle = Circle(radius)
    assert circle.s_() == expect