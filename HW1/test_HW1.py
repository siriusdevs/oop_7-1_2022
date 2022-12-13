"""
module for test calculating the characteristics (area, etc.) of a circle and a triangle
"""
import pytest
from HW1 import Triangle, Circle, TriangleException, CircleException
from typing import Union

side_transfer_test = (3, 5, 7), (5.0, 4.0, 8.0), (6.5, 8, 4)


@pytest.mark.parametrize('side_a, side_b, side_c', side_transfer_test)
def test_side_transfer(side_a: Union[float, int], side_b: Union[float, int], side_c: Union[float, int]):
    """testing raise checker for triangle

    Args:
        side_a (Union[float, int]): the first side of triangle
        side_b (Union[float, int]): the second side of triangle
        side_c (Union[float, int]): the third side of triangle
    """
    triangle = Triangle(side_a, side_b, side_c)
    assert triangle.sides[0] == side_a
    assert triangle.sides[1] == side_b
    assert triangle.sides[2] == side_c


@pytest.mark.xfail(raises=Exception)
def test_error_zero_triangle():
    """the test for sifting out the non-positive sides
    """
    with pytest.raises(TriangleException):
        Triangle(0, 4, 6.9)

    with pytest.raises(TriangleException):
        Triangle(5, -5, 6.9)


@pytest.mark.xfail(raises=Exception)
def test_error_value_triangle():
    """data type test
    """

    with pytest.raises(TriangleException):
        Triangle(5, "Koshmar", 6.9)

    with pytest.raises(TriangleException):
        Triangle(5, 5, "-6.9")


triangle_square = [(Triangle(5, 5, 8), 12.0), (Triangle(1, 1, 1), 0.43), (Triangle(10, 10, 8), 36.66)]


@pytest.mark.parametrize('triangle, expect', triangle_square)
def test_triangle_square(triangle: Triangle, expect: float):
    """Checking the correct calculation of the area of a triangle

    Args:
        triangle (Triangle): the values of the sides of the triangle
        expect (float): test area
    """
    assert triangle.square() == expect


triangle_perimetr = [(Triangle(5, 5.0, 5), 15.0), (Triangle(9, 4.5, 5), 18.5), (Triangle(12, 10, 10), 32)]


@pytest.mark.parametrize('triangle, expect', triangle_perimetr)
def test_triangle_perimetr(triangle: Triangle, expect: float):
    """Checking the correct calculation of the perimetr of a triangle

    Args:
        triangle (Triangle): the values of the sides of the triangle
        expect (float): perimetr value
    """
    assert triangle.perimetr() == expect


@pytest.mark.xfail(raises=Exception)
def test_err_negative_num_circle():
    """test for non-positive radius
    """
    with pytest.raises(CircleException):
        Circle(-1)


@pytest.mark.xfail(raises=Exception)
def test_err_data_type_circle():
    """data type test
    """
    with pytest.raises(CircleException):
        Circle("ulitka")


circle_len_test = [(Circle(10), 62.83), (Circle(16), 100.53)]


@pytest.mark.parametrize('circle, expect', circle_len_test)
def test_circle_len(circle: Circle, expect: float):
    """testing the length of the circle

    Args:
        circle (Circle): circle parameters
        expect (float): length value
    """
    assert circle.circumference() == expect


circle_square_test = [(Circle(10), 314.16), (Circle(16), 804.25)]


@pytest.mark.parametrize('circle, expect', circle_square_test)
def test_circle_square(circle: Circle, expect: float):
    """testing the square of the circle

    Args:
        circle (Circle): circle parameters
        expect (float): square value
    """
    assert circle.square() == expect
