"""Tests for classes."""

import pytest
from main import Triangle, Circle, NotValidCirc, NotValidTriang


triangles1 = [(8.0, 5.0, 5.0, True), (5.0, 5.0, 5.0, True), (7.0, 6.0, 7.0, True)]


@pytest.mark.parametrize('side1, side2, side3, exception', triangles1)
def test_validtriang1(side1: float, side2: float, side3: float, exception: bool) -> None:
    """Function test valid of triangle.

    Args:
        side1 (float): side 1 of triangle.
        side2 (float): side 2 of triangle.
        side3 (float): side 3 of triangle.
        exception (bool): expected error.
    """
    assert Triangle(side1, side2, side3).is_valid() == exception


triangles2 = [(2.0, 2.0, 3.0), (5.0, 5.0, 5.0)]


@pytest.mark.xfail(raises=NotValidTriang)
def test_validtriang2():
    """Function tests the existence of a triangle with a custom error."""
    assert Triangle(-1.0, 3.1, 3.1).is_valid()


@pytest.mark.xfail(raises=NotValidCirc)
def test_validcirc1():
    """Function tests the existence of a circle with a custom error."""
    assert Circle(-1.0).is_valid()


@pytest.mark.parametrize('side1, side2, side3', triangles2)
def test_triangle(side1: float, side2: float, side3: float):
    """Function tests if the sides of a triangle match.

    Args:
        side1 (float): side 1 of triangle.
        side2 (float): side 2 of triangle.
        side3 (float): side 3 of triangle.
    """
    triangle = Triangle(side1, side2, side3)
    assert triangle.side1 == side1
    assert triangle.side2 == side2
    assert triangle.side3 == side3


trianglesper = [(2.0, 2.0, 3.0, 7.0), (5.0, 5.0, 5.0, 15.0)]


@pytest.mark.parametrize('side1, side2, side3, answer', trianglesper)
def test_perimeter(side1: float, side2: float, side3: float, answer: float):
    """Function tests a method perimetr of triangle.

    Args:
        side1 (float): side 1 of triangle.
        side2 (float): side 2 of triangle.
        side3 (float): side 3 of triangle.
        answer (float): expected response.
    """
    triangle = Triangle(side1, side2, side3)
    assert triangle.perimeter() == answer


trianglearea = [(2.0, 2.0, 3.0, 1.98), (5.0, 5.0, 5.0, 10.83)]


@pytest.mark.parametrize('side1, side2, side3, answer', trianglearea)
def test_square(side1: float, side2: float, side3: float, answer: float):
    """Function tests a method perimetr of triangle.

    Args:
        side1 (float): side 1 of triangle.
        side2 (float): side 2 of triangle.
        side3 (float): side 3 of triangle.
        answer (float): expected response.
    """
    triangle = Triangle(side1, side2, side3)
    assert triangle.area() == answer


circles1 = [(1.0, True), (2.0, True), (7.1, True)]


@pytest.mark.parametrize('radius, exception', circles1)
def test_validcirc2(radius: float, exception: bool):
    """Function tests valid of circle.

    Args:
        radius (float): radius of circle.
        exception (bool): expected error.
    """
    assert Circle(radius).is_valid() == exception


circles2 = [(5.5), (3.4), (4.0)]


@pytest.mark.parametrize('radius', circles2)
def test_circle(radius: float):
    """Function test if the radius of circle.

    Args:
        radius (float): radius of circle.
    """
    circle = Circle(radius)
    assert circle.radius == radius


circlelen = [(5.7, 35.81), (6.3, 39.58)]


@pytest.mark.parametrize('radius, answer', circlelen)
def test_length(radius: float, answer: float):
    """Function tests a method length of circle.

    Args:
        radius (float): radius of circle.
        answer (float): expected response.
    """
    circle = Circle(radius)
    assert circle.length() == answer


circlearea = [(4.0, 50.27), (9.7, 295.59)]


@pytest.mark.parametrize('radius, answer', circlearea)
def test_c_square(radius, answer):
    """Function tests a method square of circle.

    Args:
        radius (float): radius of circle.
        answer (float): expected response
    """
    assert Circle(radius).area() == answer
