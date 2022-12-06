import pytest
from HW1 import Triangle, Circle, TriangleException, CircleException
from typing import Union

side_transfer_test = (3, 5, 8), (5.0, 4.0, 8.0), (6.5, 8, 4)


@pytest.mark.parametrize('a, b, c', side_transfer_test)
def test_side_transfer(a: Union[float, int], b: Union[float, int], c: Union[float, int]):
    triangle = Triangle(a, b, c)
    assert triangle.sides[0] == a
    assert triangle.sides[1] == b
    assert triangle.sides[2] == c


@pytest.mark.xfail(raises=Exception)
def test_error_zero_triangle():
    with pytest.raises(TriangleException):
        Triangle(0, 4, 6.9)

    with pytest.raises(TriangleException):
        Triangle(5, -5, 6.9)


@pytest.mark.xfail(raises=Exception)
def test_error_value_triangle():

    with pytest.raises(TriangleException):
        Triangle(5, "Koshmar", 6.9)

    with pytest.raises(TriangleException):
        Triangle(5, 5, "-6.9")


triangle_square = [(Triangle(5, 5, 8), 12.0), (Triangle(1, 1, 1), 0.43), (Triangle(10, 10, 8), 36.66)]


@pytest.mark.parametrize('triangle, expect', triangle_square)
def test_triangle_square(triangle: Triangle, expect: float):
    assert triangle.square() == expect


triangle_perimetr = [(Triangle(5, 5.0, 5), 15.0), (Triangle(9, 4.5, 5), 18.5), (Triangle(12, 10, 10), 32)]


@pytest.mark.parametrize('triangle, expect', triangle_perimetr)
def test_triangle_perimetr(triangle: Triangle, expect: float):
    assert triangle.perimetr() == expect


@pytest.mark.xfail(raises=Exception)
def test_err_negative_num_circle():
    with pytest.raises(CircleException):
        Circle(-1)


@pytest.mark.xfail(raises=Exception)
def test_err_data_type_circle():
    with pytest.raises(CircleException):
        Circle("ulitka")


circle_len_test = [(Circle(10), 62.83), (Circle(16), 100.53)]


@pytest.mark.parametrize('circle, expect', circle_len_test)
def test_circle_len(circle: Circle, expect: float):
    assert circle.circumference() == expect


circle_square_test = [(Circle(10), 314.16), (Circle(16), 804.25)]


@pytest.mark.parametrize('circle, expect', circle_square_test)
def test_circle_square(circle: Circle, expect: float):
    assert circle.square() == expect
