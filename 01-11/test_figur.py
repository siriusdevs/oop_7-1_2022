from figur import Triangle, Circle
import pytest


tests = [(1, 2, 3), (1, 3, 4)]


@pytest.mark.parametrize('a_side, b_side, c_side', tests)
def tests_triangle(a_side, b_side, c_side):
    triangle = Triangle(a_side, b_side, c_side)
    assert triangle.a_side == a_side
    assert triangle.b_side == b_side
    assert triangle.c_side == c_side


tests_perimetr = [(1, 2, 3, 6), (2, 6, 7, 15)]


@pytest.mark.parametrize('a_side, b_side, c_side, result', tests_perimetr)
def test_triangle_perimetr(a_side, b_side, c_side, result):
    assert Triangle(a_side, b_side, c_side).perimetr() == result


tests_area = [(2, 2, 2, 3.0), (14, 12, 18, 7040.0)]


@pytest.mark.parametrize('a_side, b_side, c_side, result', tests_area)
def test_triangle_area(a_side, b_side, c_side, result):
    assert Triangle(a_side, b_side, c_side).area() == result


tests = [(1), (2)]


@pytest.mark.parametrize('radius', tests)
def test_circle(radius):
    # circle = Circle(radius)
    # assert circle.radius == radius
    assert Circle(radius).radius == radius


tests = [(3, 28.27), (5, 78.54)]


@pytest.mark.parametrize('radius, result', tests)
def test_area_circle(radius, result):
    assert Circle(radius).area_circle() == result


tests = [(5, 31.42), (3, 18.85)]


@pytest.mark.parametrize('radius, result', tests)
def test_perimetr_circle(radius, result):
    assert Circle(radius).perimetr_circle() == result
