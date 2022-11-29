"""Testing file."""
import pytest
from dz2_oop import Circle, Triangle, NotValidFigure


def test_str_side():
    """Test string side."""
    with pytest.raises(NotValidFigure):
        Triangle('side', 3, 6)


def test_negative_side():
    """Test negative side."""
    with pytest.raises(NotValidFigure):
        Triangle(3, 9, -10)


def test_invalid_sides():
    """Test invalid sides."""
    with pytest.raises(NotValidFigure):
        Triangle(1, 5, 8)


def test_zero_sides():
    """Test zero side."""
    with pytest.raises(NotValidFigure):
        Triangle(1, 0, 8)

def test_str_radius():
    """Test string radius."""
    with pytest.raises(NotValidFigure):
        Circle('radius')


def test_negative_radius():
    """Test negative radius."""
    with pytest.raises(NotValidFigure):
        Circle(-10)


def test_zero_radius():
    """Test zero radius."""
    with pytest.raises(NotValidFigure):
        Circle(0)


test_valid_triangle = [(3.0, 4.0, 5.0, True), (1.0, 1.0, 1.0, True), (6.0, 8.0, 10.0, True)]


@pytest.mark.parametrize('side1, side2, side3, expected', test_valid_triangle)
def test_valid_tr(side1: float, side2: float, side3: float, expected: bool) -> None:
    """Test for valid triangle.
    Args:
        side1 (float): first side of triangle.
        side2 (float): second side of triangle.
        side3 (float): third side of triangle.
        expected (bool): what we expect.
    """
    assert Triangle(side1, side2, side3).is_valid() == expected


test_valid_circle = [(1.0, True), (2.0, True), (3.0, True)]


@pytest.mark.parametrize('radius, expected', test_valid_circle)
def test_valid_crle(radius: float, expected: bool) -> None:
    """Test for valid circle.
    Args:
        radius (float): circle's radius.
        expected (bool): what we wxpect.
    """
    assert Circle(radius).is_valid() == expected



test_triangle_parametrs = [(1.0, 1.0, 1.0), (5.0, 3.0, 4.0)]


@pytest.mark.parametrize('side1, side2, side3', test_triangle_parametrs)
def test_triangle(side1: float, side2: float, side3: float) -> None:
    """Test for triangle's sides. Hello.
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
    assert Circle(radius).radius == radius


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
    assert Triangle(side1, side2, side3).perimeter() == expect


test_triangle_square = [(1.0, 1.0, 1.0, 0.43), (3.0, 4.0, 5.0, 6.0)]


@pytest.mark.parametrize('side1, side2, side3, expect', test_triangle_square)
def test_square(side1: float, side2: float, side3: float, expect: float) -> None:
    """Test for triangle's square.
    Args:
        side1 (float): first side of triangle.
        side2 (float): second side of triangle.
        side3 (float): third side of triangle.
        expect (float): triangle's square.
    """
    assert Triangle(side1, side2, side3).square() == expect


test_circle_length = [(2.0, 12.57), (3.0, 18.85)]


@pytest.mark.parametrize('radius, expect', test_circle_length)
def test_length(radius: float, expect: float) -> None:
    """Test for circle's length.
    Args:
        radius (float): circle's radius.
        expect (float): circle's length.
    """
    assert Circle(radius).length() == expect


test_circle_square = [(3.0, 28.27), (2.0, 12.57)]


@pytest.mark.parametrize('radius, expect', test_circle_square)
def test_c_square(radius: float, expect: float) -> None:
    """Test for circle's square.
    Args:
        radius (float): circle's radius.
        expect (float): circle's length.
    """
    assert Circle(radius).square() == expect

