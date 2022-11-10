from classcircle import Circle
from classtriangle import Triangle
import pytest

# ТРЕУГОЛЬНИК:

# записываются ли аттрибуты:
triangle_inp_sides = [(3.0, 4.0, 5.0)]


@pytest.mark.parametrize('side1, side2, side3', triangle_inp_sides)
def test_triangle(side1: float, side2: float, side3: float) -> None:
    """Test for attributes of the triangle.

    Args:
        side1(float): 1st side of the triangle
        side2(float): 2st side of the triangle
        side3(float): 3st side of the triangle
    """
    new_triangle = Triangle(*triangle_inp_sides)
    assert new_triangle.side1 == side1
    assert new_triangle.side2 == side2
    assert new_triangle.side3 == side3

# правильно ли выполняются методы:


triangle_inp_perimeter = [(3.0, 4.0, 5.0, 12.0)]


@pytest.mark.parametrize('side1, side2, side3, res', triangle_inp_perimeter)
def test_triangle_p(side1: float, side2: float, side3: float, res: float) -> None:
    """Test for method 'perimeter' of the triangle.

    Args:
        side1(float): 1st side of the triangle
        side2(float): 2st side of the triangle
        side3(float): 3st side of the triangle
        res(float): expected result of calculations
    """
    new_triangle = Triangle(side1, side2, side3)
    assert new_triangle.perimeter() == res


triangle_inp_area = [(3.0, 4.0, 5.0, 6.0)]


@pytest.mark.parametrize('side1, side2, side3, res', triangle_inp_area)
def test_triangle_a(side1: float, side2: float, side3: float, res: float) -> None:
    """Test for method 'area' of the triangle.

    Args:
        side1(float): 1st side of the triangle
        side2(float): 2st side of the triangle
        side3(float): 3st side of the triangle
        res(float): expected result of calculations
    """
    new_triangle = Triangle(side1, side2, side3)
    assert new_triangle.area() == res


# КРУГ:

# записываются ли аттрибуты:
circle_inp_radius = [(3.0)]


@pytest.mark.parametrize('radius', circle_inp_radius)
def test_circle(radius: float) -> None:
    """Test for attributes of the circle.

    Args:
        radius(float): radius of the triangle
    """
    new_circle = Circle(radius)
    assert new_circle.radius() == radius


# правильно ли выполняются методы:
circle_inp = [(3.0, 18.85)]


@pytest.mark.parametrize('radius, res', circle_inp)
def test_circle_l(radius: float, res: float) -> None:
    """Test for method 'length_of_circle' of the circle.

    Args:
        radius(float): radius of the circle
        res(float): expected result of calculations
    """
    new_circle = Circle(radius)
    assert new_circle.length_of_circle() == res


circle_inp = [(3.0, 28.27)]


@pytest.mark.parametrize('radius, res', circle_inp)
def test_circle_a(radius: float, res: float) -> None:
    """Test for method 'area' of the circle.

    Args:
        radius(float): radius of the circle
        res(float): expected result of calculations
    """
    new_circle = Circle(radius)
    assert new_circle.area() == res
