"""Testing file."""
import pytest
from dz1_oop import Circle, Triangle


test_triangle_parametrs = [(1, 2, 3), (2, 3, 4)]


@pytest.mark.parametrize('side1, side2, side3', test_triangle_parametrs)
def test_triangle(side1: float, side2: float, side3: float) -> None:
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
def test_circle(radius: float) -> None:
    """Test for it.

    Args:
        radius (float): circle's radius.
    """
    assert Circle(radius).radius == radius


test_triangle_perimeter = [(1, 2, 3, 6), (2, 3, 4, 9)]


@pytest.mark.parametrize('side1, side2, side3, expect', test_triangle_perimeter)
def test_perimeter(side1: float, side2: float, side3: float, expect: float) -> None:
    """Test for it.

    Args:
        side1 (float): first side of triangle.
        side2 (float): second side of triangle.
        side3 (float): third side of triangle.
        expect (float): triangle's perimeter.
    """
    assert Triangle(side1, side2, side3).perimeter() == expect


test_triangle_square = [(3, 4, 5, 77.77), (1, 2, 3, 18.97)]


@pytest.mark.parametrize('side1, side2, side3, expect', test_triangle_square)
def test_square(side1: float, side2: float, side3: float, expect: float) -> None:
    """Test for it.

    Args:
        side1 (float): first side of triangle.
        side2 (float): second side of triangle.
        side3 (float): third side of triangle.
        expect (float): triangle's square.
    """
    assert Triangle(side1, side2, side3).square() == expect


test_circle_length = [(2, 12.57), (3, 18.85)]


@pytest.mark.parametrize('radius, expect', test_circle_length)
def test_length(radius: float, expect: float) -> None:
    """Test for it.

    Args:
        radius (float): circle's radius.
        expect (float): circle's length.
    """
    assert Circle(radius).length() == expect


test_circle_square = [(3, 28.27), (5, 78.54)]


@pytest.mark.parametrize('radius, expect', test_circle_square)
def test_c_square(radius: float, expect: float) -> None:
    """Test for it.

    Args:
        radius (float): circle's radius.
        expect (float): circle's length.
    """
    assert Circle(radius).square() == expect
