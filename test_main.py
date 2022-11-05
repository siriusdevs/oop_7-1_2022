"""Testing file."""
import pytest
from figures import Circle, Triangle

test_triangle_parametrs = [(1.0, 2.0, 3.0), (1.0, 3.0, 4.0)]


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


test_circle_parametrs = [(1.0), (2.0), (3.0)]


@pytest.mark.parametrize('radius', test_circle_parametrs)
def test_circle(radius: float) -> None:
    """Test for it.

    Args:
        radius (float): circle's radius.
    """
    circle = Circle(radius)
    assert circle.radius == radius


test_triangle_perimeter = [(1.0, 2.0, 3.0, 6.0), (0.1, 0.2, 0.3, 0.6)]


@pytest.mark.parametrize('side1, side2, side3, expect', test_triangle_perimeter)
def test_perimeter(side1: float, side2: float, side3: float, expect: float) -> None:
    """Test for it.

    Args:
        side1 (float): first side of triangle.
        side2 (float): second side of triangle.
        side3 (float): third side of triangle.
        expect (float): triangle's perimeter.
    """
    triangle = Triangle(side1, side2, side3)
    assert triangle.perimeter() == expect


test_triangle_square = [(2.0, 3.0, 4.0, 2.9047375096555625), (3.0, 4.0, 5.0, 6.0)]


@pytest.mark.parametrize('side1, side2, side3, expect', test_triangle_square)
def test_square(side1: float, side2: float, side3: float, expect: float) -> None:
    """Test for it.

    Args:
        side1 (float): first side of triangle.
        side2 (float): second side of triangle.
        side3 (float): third side of triangle.
        expect (float): triangle's square.
    """
    triangle = Triangle(side1, side2, side3)
    assert triangle.square() == expect


test_circle_length = [(2.0, 12.566370614359172), (3.0, 28.274333882308138)]


@pytest.mark.parametrize('radius, expect', test_circle_length)
def test_length(radius: float, expect: float) -> None:
    """Test for it.

    Args:
        radius (float): circle's radius.
        expect (float): circle's length.
    """
    circle = Circle(radius)
    assert circle.length() == expect


test_circle_square = [(3.0, 18.84955592153876), (2.0, 12.566370614359172)]


@pytest.mark.parametrize('radius, expect', test_circle_square)
def test_c_square(radius: float, expect: float) -> None:
    """Test for it.

    Args:
        radius (float): circle's radius.
        expect (float): circle's length.
    """
    circle = Circle(radius)
    assert circle.square() == expect
