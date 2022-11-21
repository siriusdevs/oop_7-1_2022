from figures import Triangle
from figures import Circle
import pytest

test_triangle = [[1.0, 2.0, 2.0], [6.0, 6.0, 6.0]]


@pytest.mark.parametrize('sides', test_triangle)
def test_triangle(sides):
    tr = Triangle(sides)
    assert tr.sides == sides


@pytest.mark.xfail(raises=Exception)
def test_incorrect_sides():
    with pytest.raises(Exception):
        Triangle([1, 1, 4])

    with pytest.raises(Exception):
        Triangle([2, 0, 2])
    
    with pytest.raises(Exception):
        Triangle([1000, -7, 0])
    
    with pytest.raises(Exception):
        Triangle([1000, -7, "ya gul..."])


tests_triangle_square = [(Triangle([1, 1, 1]), 0.43), (Triangle([2, 2, 3]), 1.98), (Triangle([2, 3, 4]), 2.9)]


@pytest.mark.parametrize('triangle, expect', tests_triangle_square)
def test_triangle_square(triangle: Triangle, expect: float) -> None:
    assert triangle.square() == expect


tests_triangle_perimeter = [(Triangle([1, 1, 1]), 3), (Triangle([2, 2, 3]), 7), (Triangle([2, 3, 4]), 9)]


@pytest.mark.parametrize('triangle, expect', tests_triangle_perimeter)
def test_triangle_perimeter(triangle: Triangle, expect: int) -> None:
    assert triangle.perimetr() == expect


tests_circle_create = [1.0, 2.0, 3.0]


@pytest.mark.parametrize('radius', tests_circle_create)
def test_circle(radius: float) -> None:
    circle = Circle(radius)
    assert circle.radius == radius


@pytest.mark.xfail(raises=Exception)
def test_err_invalid_circle():
    with pytest.raises(Exception):
        Circle(-5)


@pytest.mark.xfail(raises=Exception)
def test_err_value_circle():
    with pytest.raises(Exception):
        Circle("voronezh")


tests_circle_len = [(Circle(4), 50.27), (Circle(2), 12.57), (Circle(3), 28.27)]


@pytest.mark.parametrize('circle, expect', tests_circle_len)
def test_circle_len(circle: Circle, expect: float) -> None:
    assert circle.len_circle() == expect


tests_circle_square = [(Circle(4), 25.13), (Circle(2), 12.57), (Circle(3), 18.85)]


@pytest.mark.parametrize('circle, expect', tests_circle_square)
def test_circle_square(circle: Circle, expect: float) -> None:
    assert circle.square() == expect
