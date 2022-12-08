"""This file for triangle class."""
from typing import List
from exeptions_for_triangle import TriangleInvalidSides
from math import sqrt


class Triangle(object):
    """
    This class create triangle.
    Данный класс создаёт треугольник.
    """

    def __init__(self, side_a: float or int, side_b: float or int, side_c: float or int) -> None:
        """
        This method creates a triangle.
        Этот метод создаёт треугольник.
        Args:
            side_a: float or int side.
            десятичная или целочисленная сторона
            side_b: float or int side.
            десятичная или целочисленная сторона
            side_c: float or int side.
            десятичная или целочисленная сторона
        """
        self.sides = [side_a, side_b, side_c]

    @classmethod
    def validation_triangle(cls, side_a: float or int, side_b: float or int, side_c: float or int) -> bool:
        """
        This method checks if such a triangle exists.
        Этот метод проверяет существует-ли такой треугольник, а также правильность введенения данных.
        Args:
            side_a: float First side.
            десятичное число - Первая сторона.
            side_b: float Second side.
            десятичное число - Вторая сторона.
            side_c: float Third side.
            десятичное число - Третья сторона.
        Return:
            bool: if triangle is exist or ist exist
            логический - когда треугольник существует или нет
        Raises:
            ValueError: if any of the sides is not float or int or <= 0.
            Если любая сторона не десятичная или не целочисленная или меньше или равна 0.
            InvalidTriangleSides: if triangle can't exist.
            Если такой треугольник не существует.
        """
        if not isinstance(side_a, (float, int)) \
                or not isinstance(side_b, (float, int)) \
                or not isinstance(side_c, (float, int)):
            raise ValueError("Sides must be float or int / Стороны должны быть целочисленные или десятичные")
        elif side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Sides must be not zero / Стороны не должны быть нулевыми")
        elif not (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
            raise TriangleInvalidSides([side_a, side_b, side_c])
        return True

    @property
    def sides(self) -> List[float]:
        """
        Get current values of sides.
        Возвращает настоящее значение сторон.
        Returns:
            List[float] - current value of sides.
            Список десятичных чисел - настоящее значение сторон.
        """
        return self._sides

    @sides.setter
    def sides(self, new_sides: List[float or int]) -> None:
        """
        Sets a new sides.
        Устанавливает новые стороны.
        Args:
            new_sides: list of float values - new values of sides.
            Список десятичных чисел - новое значение сторон.
        Raises:
            ValueError: If a triangle has more or less than three sides.
        """
        value_of_sides = 3
        if len(new_sides) == value_of_sides:
            if self.validation_triangle(new_sides[0], new_sides[1], new_sides[2]):
                self._sides = new_sides
        else:
            raise ValueError("Triangle always has 3 sides. / У треугольника всегда 3 стороны.")

    def get_perimeter(self) -> float:
        """
        Calculates the perimeter of a triangle and returns the value rounded to two decimal places.
        Считает периметр треугольника и возвращает округлённое до двух знаков после заяпятой значение.
        Returns:
            float - triangle perimeter rounded to two decimal places.
            десятичное число - периметр треугольника округлённый до двух знаков после запятой.
        """
        return round(self.sides[0] + self.sides[1] + self.sides[2], 2)

    def get_square(self) -> float:
        """
        Counts and rounds to 2 decimal places the square of the triangle.
        Считает и округляет до 2-х точек после запятой площадь треугольника
        Returns:
            float - area of a triangle rounded to two decimal places.
            десятичное число - площадь треугольника округлённая до двух знаков после запятой.
        """
        half_perimetr = self.get_perimeter() / 2
        square = sqrt(
            half_perimetr * (half_perimetr - self.sides[0])
            * (half_perimetr - self.sides[1])
            * (half_perimetr - self.sides[2]))
        return round(square, 2)
