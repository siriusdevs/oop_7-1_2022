"""Tests for classes of figures."""
import pytest
from figures import Circle, InvalidFigureError, Triangle

# Tests for Triangle class.


def test_str_side():
    """Test string side."""
    with pytest.raises(InvalidFigureError):
        Triangle('side', 3, 6)


def test_negative_side():
    """Test negative side."""
    with pytest.raises(InvalidFigureError):
        Triangle(3, 9, -10)


def test_invalid_sides():
    """Test invalid sides."""
    with pytest.raises(InvalidFigureError):
        Triangle(1, 5, 8)


def test_zero_sides():
    """Test zero side."""
    with pytest.raises(InvalidFigureError):
        Triangle(1, 0, 8)


tests_triangle_init = [(3, 9, 7), (4, 2, 5), (19, 14, 11)]


@pytest.mark.parametrize('side1, side2, side3', tests_triangle_init)
def test_init_triangle(side1: int, side2: int, side3: int) -> None:
    """Test triangle's initialization."""
    triangle = Triangle(side1, side2, side3)
    assert triangle.side1 == side1
    assert triangle.side2 == side2
    assert triangle.side3 == side3


tests_triangle_perimeter = [(3, 9, 7, 19), (4, 2, 5, 11), (19, 14, 11, 44)]


@pytest.mark.parametrize('side1, side2, side3, answer', tests_triangle_perimeter)
def test_perimeter_triangle(side1: int, side2: int, side3: int, answer: int) -> None:
    """Test triangle's perimeter method."""
    assert Triangle(side1, side2, side3).perimeter() == answer


tests_triangle_area = [(3, 9, 7, 8.79), (4, 2, 5, 3.8), (19, 14, 11, 76.21)]


@pytest.mark.parametrize('side1, side2, side3, answer', tests_triangle_area)
def test_area_triangle(side1: int, side2: int, side3: int, answer: float) -> None:
    """Test triangle's area method."""
    assert Triangle(side1, side2, side3).area() == answer


# Tests for Circle class.


def test_str_radius():
    """Test string radius."""
    with pytest.raises(InvalidFigureError):
        Circle('radius')


def test_negative_radius():
    """Test negative radius."""
    with pytest.raises(InvalidFigureError):
        Circle(-10)


def test_zero_radius():
    """Test zero radius."""
    with pytest.raises(InvalidFigureError):
        Circle(0)


tests_circle_init = [(4), (67), (16)]


@pytest.mark.parametrize('radius', tests_circle_init)
def test_init_circle(radius: int) -> None:
    """Test circle's initialization."""
    assert Circle(radius).radius == radius


tests_circle_length = [(4, 25.13), (67, 420.97), (16, 100.53)]


@pytest.mark.parametrize('radius, answer', tests_circle_length)
def test_length_circle(radius: int, answer: float) -> None:
    """Test circle's lenghth method."""
    assert Circle(radius).length() == answer


tests_circle_area = [(4, 50.27), (67, 14102.61), (16, 804.25)]


@pytest.mark.parametrize('radius, answer', tests_circle_area)
def test_area_circle(radius: int, answer: float) -> None:
    """Test circle's area method."""
    assert Circle(radius).area() == answer
