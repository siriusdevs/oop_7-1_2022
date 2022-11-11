"""Testing file."""
import pytest
from figures import Circle, Triangle, NotValidFigure

test_valid_triangle = [(5.0, 4.0, 3.0, True), (1.0, 1.0, 1.0, True), (6.0, 8.0, 10.0, True)]


@pytest.mark.parametrize('side1, side2, side3, expectation', test_valid_triangle)
def test_valid_tr(side1: float, side2: float, side3: float, expectation: bool) -> None:
    """Test for valid triangle.

    Args:
        side1 (float): first side of triangle.
        side2 (float): second side of triangle.
        side3 (float): third side of triangle.
        expectation (bool): what we wxpect.
    """
    assert Triangle(side1, side2, side3).is_valid() == expectation


@pytest.mark.xfail(raises=NotValidFigure)
def test_val_tr():
    """Test for not existing triangle."""
    first_side = -1.0
    second_side = 5.0
    third_side = 4.0
    expectation = False
    assert Triangle(first_side, second_side, third_side).is_valid() == expectation


test_valid_circle = [(1.0, True), (2.0, True), (3.0, True)]


@pytest.mark.parametrize('radius, expectation', test_valid_circle)
def test_valid_crle(radius: float, expectation: bool) -> None:
    """Test for valid circle.

    Args:
        radius (float): circle's radius.
        expectation (bool): what we wxpect.
    """
    assert Circle(radius).is_valid() == expectation


@pytest.mark.xfail(raises=NotValidFigure)
def test_val_cr():
    """Test for not existing triangle."""
    radius = -1
    expectation = False
    assert Circle(radius).is_valid() == expectation


test_triangle_parametrs = [(1.0, 1.0, 1.0), (5.0, 3.0, 4.0)]


@pytest.mark.parametrize('side1, side2, side3', test_triangle_parametrs)
def test_triangle(side1: float, side2: float, side3: float) -> None:
    """Test for triangle's sides.

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
    """Test for circle's radius.

    Args:
        radius (float): circle's radius.
    """
    circle = Circle(radius)
    assert circle.radius == radius


test_triangle_perimeter = [(1.0, 1.0, 1.0, 3.0), (0.3, 0.4, 0.5, 1.2)]


@pytest.mark.parametrize('side1, side2, side3, expect', test_triangle_perimeter)
def test_perimeter(side1: float, side2: float, side3: float, expect: float) -> None:
    """Test for triangle's perimeter.

    Args:
        side1 (float): first side of triangle.
        side2 (float): second side of triangle.
        side3 (float): third side of triangle.
        expect (float): triangle's perimeter.
    """
    triangle = Triangle(side1, side2, side3)
    assert triangle.perimeter() == expect


test_triangle_square = [(1.0, 1.0, 1.0, 0.43301), (3.0, 4.0, 5.0, 6.0)]


@pytest.mark.parametrize('side1, side2, side3, expect', test_triangle_square)
def test_square(side1: float, side2: float, side3: float, expect: float) -> None:
    """Test for triangle's square.

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
    """Test for circle's length.

    Args:
        radius (float): circle's radius.
        expect (float): circle's length.
    """
    circle = Circle(radius)
    assert circle.length() == expect


test_circle_square = [(3.0, 18.84955592153876), (2.0, 12.566370614359172)]


@pytest.mark.parametrize('radius, expect', test_circle_square)
def test_c_square(radius: float, expect: float) -> None:
    """Test for circle's square.

    Args:
        radius (float): circle's radius.
        expect (float): circle's length.
    """
    circle = Circle(radius)
    assert circle.square() == expect
