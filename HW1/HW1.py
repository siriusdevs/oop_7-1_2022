"""Module for calculating the characteristics (area, etc.) of a circle and a triangle."""
from typing import Union
from math import sqrt, pi


class TriangleException(Exception):
    """A class with a custom error for the triangle."""
    def __init__(self, message):
        """Init msg for triangle raise.

        Args:
            message (str): _description_.
        """
        self.message = message

    def __str__(self):
        return self.message


class CircleException(Exception):
    """A class with a custom error for the circle."""
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Triangle:
    """A class for creating and calculating triangle properties."""

    def __init__(self, side_a: Union[float, int], side_b: Union[float, int], side_c: Union[float, int]):
        """Creating a triangle.

        Args:
            side_a (Union[float, int]): first side of the triangle
            side_b (Union[float, int]): second side of the triangle
            side_c (Union[float, int]): third side of the triangle
            sides (list): the list of sides of the triangle, includes a[0], b[1], c[2].
        """
        self.__sides = [side_a, side_b, side_c]
        self.checker(self.sides)

    def checker(self, sides):
        """Error checker for triangle.

        Args:
            sides (list): the list of sides of the triangle, includes a[0], b[1], c[2].

        Raises:
            TriangleException: does not match the numeric data type
            TriangleException: checks the number of sides in a triangle
            TriangleException: does not conform to the rules of the triangle
            TriangleException: negative numbers cannot be the length of a side.
        """
        if not all([isinstance(side, (float, int)) for side in sides]):
            raise TriangleException("Неверный формат данных")
        if len(sides) != 3:
            raise TriangleException("Не хватает сторон")
        if not (sorted(sides)[2] < sorted(sides)[0] + sorted(sides)[1]):
            raise TriangleException("Такой треугольник не построить")
        if all(sides[side] <= 0 for side in range(2)):
            raise TriangleException("Чумба, сходи попей колесики, а потом задавая отрицательные числа для сторон")

    @property
    def sides(self):
        """Getter for sides."""
        return self.__sides

    @sides.setter
    def sides(self, sides):
        """Setter for sides.

        Args:
            sides (list): the list of sides of the triangle, includes a[0], b[1], c[2].
        """
        self.checker(sides)
        self.__sides = sides

    def perimetr(self):
        """Calculating the rounded perimeter of a triangle.

        Returns:
            float: perimetr of triangle.
        """
        return round((self.__sides[0] + self.__sides[1] + self.__sides[2]), 2)

    def square(self):
        """Calculating the rounded area of a triangle.

        Returns:
            float: square of triangle.
        """
        p = self.perimetr() * 0.5
        return round((sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))), 2)


class Circle:
    """A class for creating and calculating circle properties."""
    def __init__(self, radius: Union[float, int]):
        """Creating a circle.

        Args:
            radius (Union[float, int]): radius of a circle.
        """
        self.__radius = radius
        self.checker(self.radius)

    def checker(self, radius):
        """Error checker for circle.

        Args:
            radius (Union[float, int]): radius of a circle.

        Raises:
            CircleException: check for a negative number
            CircleException: data format check.
        """
        if not isinstance(radius, Union[float, int]):
            raise CircleException("Неверный формат данных")
        if radius <= 0:
            raise CircleException("Такую окружность не построить")

    @property
    def radius(self):
        """Getter for radius."""
        return self.__radius

    @radius.setter
    def radius(self, radius: Union[float, int]):
        """Setter for radius.

        Args:
            radius (Union[float, int]): radius of a circle.
        """
        self.checker(radius)
        self.__radius = radius

    def circumference(self):
        """Rounded circle length calculation.

        Returns:
            float: circle length.
        """
        return round((2 * pi * self.__radius), 2)

    def square(self):
        """Rounded circle area calculation.

        Returns:
            float: circle area.
        """
        return round((pi * self.__radius ** 2), 2)
