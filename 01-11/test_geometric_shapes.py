"""Tests for geometric_shapes."""

import pytest

from models.geometric_shapes import Circle, Triangle
from models.exceptions import InvalidTriangleSides, InvalidCircleRadius

tests_triangle_create = [(2.0, 2.0, 3.0), (1.0, 1.0, 1.0), (2, 3, 4)]


@pytest.mark.parametrize('side_a, side_b, side_c', tests_triangle_create)
def test_triangle_create(side_a: float, side_b: float, side_c: float) -> None:
    """Test for create triangle.

    Args:
        side_a: float -  first side of triangle.
        side_c: float -  second side of triangle.
        side_b: float - third side of triangle.
    """
    triangle = Triangle(side_a, side_b, side_c)
    assert triangle.side_a == side_a
    assert triangle.side_b == side_b
    assert triangle.side_c == side_c


@pytest.mark.xfail(raises=InvalidTriangleSides)
def test_err_invalid_triangle():
    """Tests for triangles' InvalidTriangleSides."""
    with pytest.raises(InvalidTriangleSides):
        Triangle(1, 1, 4)

    with pytest.raises(InvalidTriangleSides):
        Triangle(100, 1, 8)


@pytest.mark.xfail(raises=ValueError)
def test_err_value_triangle():
    """Tests for triangles' ValuerError."""
    with pytest.raises(ValueError):
        Triangle(1, 1, "20.01 soon")

    with pytest.raises(ValueError):
        Triangle(1, 1, -100)


tests_triangle_square = [(Triangle(1, 1, 1), 0.43), (Triangle(2, 2, 3), 1.98), (Triangle(2, 3, 4), 2.9)]


@pytest.mark.parametrize('triangle, expect', tests_triangle_square)
def test_triangle_square(triangle: Triangle, expect: float) -> None:
    """Test for triangles' square.

    Args:
        triangle: triangle - the triangle.

        expect: float - triangle's square.
    """
    assert triangle.get_square() == expect


tests_triangle_perimeter = [(Triangle(1, 1, 1), 3), (Triangle(2, 2, 3), 7), (Triangle(2, 3, 4), 9)]


@pytest.mark.parametrize('triangle, expect', tests_triangle_perimeter)
def test_triangle_perimeter(triangle: Triangle, expect: float) -> None:
    """Test for triangles' perimeter.

    Args:
        triangle: triangle - the triangle.

        expect: float - triangle's perimeter.
    """
    assert triangle.get_perimeter() == expect


tests_circle_create = [1.0, 2.0, 3.0]


@pytest.mark.parametrize('radius', tests_circle_create)
def test_circle(radius: float) -> None:
    """Test for circle's radius.

    Args:
        radius: float - circle's radius.
    """
    circle = Circle(radius)
    assert circle.radius == radius


@pytest.mark.xfail(raises=InvalidCircleRadius)
def test_err_invalid_circle():
    """Tests for circles' InvalidCircleRadius."""
    with pytest.raises(InvalidCircleRadius):
        Circle(-5)


@pytest.mark.xfail(raises=ValueError)
def test_err_value_circle():
    """Tests for circles' InvalidCircleRadius."""
    with pytest.raises(InvalidCircleRadius):
        Circle("ja radius pusti")


tests_circle_len = [(Circle(4), 25.13), (Circle(2), 12.57), (Circle(3), 18.85)]


@pytest.mark.parametrize('circle, expect', tests_circle_len)
def test_circle_len(circle: Circle, expect: float) -> None:
    """Test for circle's len.

    Args:
        circle: circle - the circle.

        expect: float - circle's len.
    """
    assert circle.get_len_circle() == expect


tests_circle_square = [(Circle(4), 50.27), (Circle(2), 12.57), (Circle(3), 28.27)]


@pytest.mark.parametrize('circle, expect', tests_circle_square)
def test_circle_square(circle: Circle, expect: float) -> None:
    """Test for circle's square.

    Args:
        circle: circle - the circle.

        expect: float - circle's square.
    """
    assert circle.get_square() == expect
