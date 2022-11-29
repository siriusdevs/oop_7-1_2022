from typing import List

import pytest
from triangle import Triangle
from exeptions_for_triangle import TriangleInvalidSides

tests_create_triangle = [([4.0, 4.0, 6.0]), ([1.0, 1.0, 1.0]), ([3, 4, 5])]


@pytest.mark.parametrize('sides', tests_create_triangle)
def test_triangle_create(sides: List[float or int]) -> None:
    """
    Test for create triangle.
    Тесты создания треугольника.
    Args:
        sides: list of float - sides of triangle.
        список десятичных чисел - стороны треугольника.
    """
    triangle = Triangle(*sides)
    assert triangle.sides == sides


@pytest.mark.xfail(raises=TriangleInvalidSides)
def test_invalid_triangle_create():
    """
    Tests for raises triangles exeption TriangleInvalidSides.
    Тесты для вызова ошибок TriangleInvalidSides у треугольников.
    """
    with pytest.raises(TriangleInvalidSides):
        Triangle(1, 1, 4)

    with pytest.raises(TriangleInvalidSides):
        Triangle(100, 1, 8)

    with pytest.raises(TriangleInvalidSides):
        Triangle(1, 11.5, 2)


@pytest.mark.xfail(raises=ValueError)
def tests_err_value_triangle():
    """
    Tests for raises triangles ValuerError.
    Тесты вызова у треугольников ошибок ValuerError.
    """
    with pytest.raises(ValueError):
        Triangle("2", 1, "1")

    with pytest.raises(ValueError):
        Triangle(-40, 1, -100)

    with pytest.raises(ValueError):
        Triangle(0, 2, "7")


tests_perimetr = [(Triangle(1, 1, 1), 3), (Triangle(2.5, 3, 4.1), 9.6)]


@pytest.mark.parametrize("triangle, expect", tests_perimetr)
def tests_to_find_perimetr(triangle: Triangle, expect: float) -> None:
    """
    Tests for the correct calculation of the perimeter of a triangles.
    Тесты на правильность подсчёта периметра треугольников.
    """
    assert triangle.get_perimeter() == expect


tests_square = [(Triangle(1, 1, 1.5), 0.5), (Triangle(2.5, 3, 1.1), 1.32)]


@pytest.mark.parametrize("triangle, expect", tests_square)
def tests_to_find_square(triangle: Triangle, expect: float) -> None:
    """
    Tests for the correctness of calculating the square of the triangles.
    Тесты на правильность подсчёта площади треугольников.
    """
    assert triangle.get_square() == expect
