# test
import pytest
from dz1_oop import Circle, Triangle

test_triangle_data = [(3, 4, 5)]


@pytest.mark.parametrize('side1, side2, side3', test_triangle_data)
def test_triangle(side1, side2, side3):
    triangle = Triangle(side1, side2, side3)
    assert triangle.side1 == side1
    assert triangle.side2 == side2
    assert triangle.side3 == side3


test_circle_data = [(2)]


@pytest.mark.parametrize('r', test_circle_data)
def test_circle(r):
    circle = Circle(r)
    assert circle.r == r


test_triangle_p_ = [(1, 2, 3, 6)]


@pytest.mark.parametrize('side1, side2, side3, expect', test_triangle_p_)
def test_p_(side1, side2, side3, expect):
    triangle = Triangle(side1, side2, side3)
    assert triangle.p_() == expect


test_triangle_s_ = [(3, 4, 5, 77.77)]


@pytest.mark.parametrize('side1, side2, side3, expect', test_triangle_s_)
def test_triangle_s(side1, side2, side3, expect):
    triangle = Triangle(side1, side2, side3)
    assert triangle.s_() == expect


test_circle_l_ = [(2, 12.57)]


@pytest.mark.parametrize('r, expect', test_circle_l_)
def test_length(r, expect):
    circle = Circle(r)
    assert circle.l_() == expect


test_circle_s_ = [(3, 28.27)]


@pytest.mark.parametrize('r, expect', test_circle_s_)
def test_circle_s_(r, expect):
    circle = Circle(r)
    assert circle.s_() == expect