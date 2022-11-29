"""This file for exceptions triangle."""
from typing import List


class TriangleInvalidSides(Exception):
    """
    Exception for non-existent triangle.
    Ошибка несуществующего треугольника.
    """

    def __init__(self, sides: List[float or int]) -> None:
        """
        Exception for create or edit triangle.
        Ошибка создания или изменения треугольника.
        Args:
            sides: list - of sides of a triangle.
            список - список со сторонами треугольника.
        """
        super().__init__("Triangle with sides: {0}, {1}, {2} - can't exist" +
                         "Треугольник со сторонами: {0}, {1}, {2} - не существует".format(*sides))


class InvalidCountSidesOfTriangle(Exception):
    """
    Exeption of invalid count sides of triangle.
    Ошибка неправильности количесва сторон в треугольнике.
    """

    def __init__(self, sides: List[float or int]) -> None:
        """
        Exception for create or edit triangle.
        Ошибка создания или изменения треугольника.
        Args:
            sides: list - of sides of a triangle.
            список - список со сторонами треугольника.
        """
        super().__init__("Invalid count of sides in triangle: {0} / " +
                         "Неправильное количество сторон треугольника: {0}".format(sides))
