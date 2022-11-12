import pytest

from main import Triangle, Circle, NotValidCirc, NotValidTriang

triangles_1 = [(8.0, 5.0, 5.0, True), (5.0, 5.0, 5.0, True), (7.0, 6.0, 7.0, True)]

@pytest.mark.parametrize('side1, side2, side3, exception', triangles_1)
def test_valid_triang_1(side1, side2, side3, exception):
    assert Triangle(side1, side2, side3).is_valid() == exception

triangles_2 = [(2.0, 2.0, 3.0), (5.0, 5.0, 5.0)]

@pytest.mark.xfail(raises=NotValidTriang)
def test_valid_triang_2():
    Triangle(-1.0, 2.0, 2.0).is_valid()

@pytest.mark.xfail(raises=NotValidCirc)
def test_valid_circ_1():
    Circle(-1.0).is_valid()

@pytest.mark.parametrize('side1, side2, side3', triangles_2)
def test_triangle(side1, side2, side3):
    triangle = Triangle(side1, side2, side3)
    assert triangle.side1 == side1
    assert triangle.side2 == side2
    assert triangle.side3 == side3

triangles_per = [(2.0, 2.0, 3.0, 7.0), (5.0, 5.0, 5.0, 15.0)]

@pytest.mark.parametrize('side1, side2, side3, answer', triangles_per)
def test_perimeter(side1, side2, side3, answer):
    triangle = Triangle(side1, side2, side3)
    assert triangle.perimeter() == answer

triangle_area = [(2.0, 2.0, 3.0, 1.98), (5.0, 5.0, 5.0, 10.83)]

@pytest.mark.parametrize('side1, side2, side3, answer', triangle_area)
def test_square(side1, side2, side3, answer):
    triangle = Triangle(side1, side2, side3)
    assert triangle.area() == answer

circles_1 = [(1.0, True), (2.0, True), (7.1, True)]

@pytest.mark.parametrize('radius, exception', circles_1)
def valid_circ_2(radius, exception):
    assert Circle(radius).is_valid() == exception

circles_2 = [(5.5), (3.4), (4.0)]

@pytest.mark.parametrize('radius', circles_2)
def test_circle(radius):
    circle = Circle(radius)
    assert circle.radius == radius

circle_len = [(5.7, 35.81), (6.3, 39.58)]

@pytest.mark.parametrize('r, answer', circle_len)
def test_length(r, answer):
    circle = Circle(r)
    assert circle.length() == answer

circle_area = [(4.0, 50.27), (9.7, 295.59)]

@pytest.mark.parametrize('radius, answer', circle_area)
def test_c_square(radius, answer):
    circle = Circle(radius)
    assert circle.area() == answer