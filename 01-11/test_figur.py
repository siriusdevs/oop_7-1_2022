from figur import Triangle, Circle
import pytest



tests = [(1, 2, 3), (1, 3, 4)]

@pytest.mark.parametrize('a, b, c', tests)
def tests_triangle(a, b, c):
    triangle = Triangle(a, b, c)
    assert triangle.a == a
    assert triangle.b == b
    assert triangle.c == c



tests_perimetr = [(1, 2, 3, 6), (2, 6, 7, 15)]

@pytest.mark.parametrize('a, b, c, result', tests_perimetr)
def test_triangle_perimetr(a, b, c, result):
    triangle = Triangle(a, b, c)
    assert triangle.perimetr() == result



tests_area = [(6, 8, 10, 24), (3, 4, 5, 6)]


@pytest.mark.parametrize('a, b, c, result', tests_area)
def test_triangle_area(a, b, c, result):
    triangle = Triangle(a, b, c)
    assert triangle.area() == result



tests = [(1), (2)]

@pytest.mark.parametrize('r', tests)
def test_circle(r):
    circle = Circle(r)
    assert circle.r == r


tests = [(3, 28.3), (2, 12.6)]

@pytest.mark.parametrize('r, result', tests)
def test_area_circle(r, result):
    circle = Circle(r)
    assert circle.area_circle() == result


tests = [(2, 12.6), (3, 18.8)]


@pytest.mark.parametrize('r, result', tests)
def test_perimetr_circle(r, result):
    circle = Circle(r)
    assert circle.perimetr_circle() == result