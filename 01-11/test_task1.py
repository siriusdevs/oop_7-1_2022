"""File with tests for figure classes."""
from task01 import Triangle, Circle
import pytest


check_tr = [(3, 4, 5), (13, 40, 15), (3.45, 4.53, 5.34)]


@pytest.mark.parametrize('side1, side2, side3', check_tr)
def test_triangle(side1: float, side2: float, side3: float):
    """Test initialization method for triangle."""
    triangle = Triangle(side1, side2, side3)
    assert triangle.side1 == side1
    assert triangle.side2 == side2
    assert triangle.side3 == side3


check_tr_per = [(3, 4, 5, 12), (13, 20, 15, 48), (3.45, 4.53, 5.34, 13.32)]


@pytest.mark.parametrize('side1, side2, side3, back', check_tr_per)
def test_triangle_perimeter(side1: float, side2: float, side3: float, back: float):
    """This test check the perimeter of the triangle."""
    assert Triangle(side1, side2, side3).perimeter() == back


check_tr_area = [(3, 4, 5, 6), (13, 20, 15, 97.49), (3.45, 4.53, 5.34, 7.75)]


@pytest.mark.parametrize('side1, side2, side3, back', check_tr_area)
def test_triangle_area(side1: float, side2: float, side3: float, back: float):
    """This test check the area of the triangle."""
    assert Triangle(side1, side2, side3).area() == back


check_circle = [(5,), (4.4,), (200,)]


@pytest.mark.parametrize('radius', check_circle)
def test_circle(radius: float):
    """Test initialization method for circle."""
    circle = Circle(radius)
    assert circle.radius == radius


check_cir_len = [(5, 31.42), (4.4, 27.65), (200, 1256.64)]


@pytest.mark.parametrize('radius, back', check_cir_len)
def test_circle_length(radius: float, back: float):
    """This test check the length of the circle."""
    circle = Circle(radius)
    assert circle.length() == back


check_cir_area = [(5, 78.54), (4.4, 60.82), (200, 125663.71)]


@pytest.mark.parametrize('radius, back', check_cir_area)
def test_circle_area(radius: float, back: float):
    """This test check the area of the circle."""
    circle = Circle(radius)
    assert circle.area() == back
