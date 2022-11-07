"""Tests for classes of figures."""
from figures import Triangle, Circle
import pytest
APPROX_VALUE = 0.01  # specifies approx value

# Tests for Triangle class.

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


tests_triangle_area = [(3, 9, 7, 8.78), (4, 2, 5, 3.8), (19, 14, 11, 76.21)]


@pytest.mark.parametrize('side1, side2, side3, answer', tests_triangle_area)
def test_area_triangle(side1: int, side2: int, side3: int, answer: float) -> None:
    """Test triangle's area method."""
    assert Triangle(side1, side2, side3).area() == pytest.approx(answer, rel=APPROX_VALUE)


# Tests for Circle class.

tests_circle_init = [(4), (67), (16)]


@pytest.mark.parametrize('radius', tests_circle_init)
def test_init_circle(radius: int) -> None:
    """Test circle's initialization."""
    circle = Circle(radius)
    assert circle.radius == radius


tests_circle_length = [(4, 25.13), (67, 420.97), (16, 100.53)]


@pytest.mark.parametrize('radius, answer', tests_circle_length)
def test_length_circle(radius: int, answer: float) -> None:
    """Test circle's lenghth method."""
    assert Circle(radius).length() == pytest.approx(answer, rel=APPROX_VALUE)


tests_circle_area = [(4, 50.24), (67, 14095.46), (16, 803.84)]


@pytest.mark.parametrize('radius, answer', tests_circle_area)
def test_area_circle(radius: int, answer: float) -> None:
    """Test circle's area method."""
    assert Circle(radius).area() == pytest.approx(answer, rel=APPROX_VALUE)
