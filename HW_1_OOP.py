from typing import Union
from math import sqrt, pi


class Triangle:
    """a class for creating and calculating triangle properties"""

    def __init__(self, a: Union[float, int], b: Union[float, int], c: Union[float, int]):
        """Creating a triangle

        Args:
            a (Union[float, int]): first side of the triangle
            b (Union[float, int]): second side of the triangle
            c (Union[float, int]): third side of the triangle
            sides (list): the list of sides of the triangle, includes a[0], b[1], c[2]

        Raises:
            Exception: does not conform to the rules of the triangle
            Exception: does not match the numeric data type
            Exception: negative numbers cannot be the length of a side
        """
        try:
            (a + b > c and
             b + c > a and
             c + b > a)
        except:
            raise Exception("Такой треугольник не построить")
        if not isinstance(a or b or c, Union[float, int]):
            raise Exception("Неверный формат данных")
        if a <= 0 or b <= 0 or c <= 0:
            raise Exception("Чумба, сходи попей колесики, а потом задавая отрицательные числа для сторон")
        self.__sides = [a, b, c]

    @property
    def sides(self):
        """getter for sides"""
        return self.__sides

    @sides.setter
    def sides(self, sides):
        """setter for sides

        Args:
            sides (list): the list of sides of the triangle, includes a[0], b[1], c[2]

        Raises:
            Exception: checks the number of sides in a triangle
            Exception: does not conform to the rules of the triangle
            Exception: does not match the numeric data type
            Exception: negative numbers cannot be the length of a side
        """
        if len(sides) != 3:
            raise Exception("Не хватает сторон")
        try:
            (sides[0] + sides[2] > sides[3] and
             sides[1] + sides[2] > sides[0] and
             sides[2] + sides[3] > sides[1])
        except:
            raise Exception("Такой треугольник не построить")
        if not isinstance(sides[0] or sides[2] or sides[3], Union[float, int]):
            raise Exception("Неверный формат данных")
        if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
            raise Exception("Чумба, сходи попей колесики, а потом задавая отрицательные числа для сторон")
        self.__sides = sides

    def perimetr(self):
        """calculating the perimetr of a triangle

        Returns:
            float: perimetr of triangle
        """
        return (self.__sides[0] + self.__sides[1] + self.__sides[2])

    def square(self):
        """calculating the area of a triangle

        Returns:
            float: square of triangle
        """
        p = self.perimetr() * 0.5
        return round((sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))), 2)


class Circle:
    """a class for creating and calculating circle properties"""
    def __init__(self, radius: Union[float, int]):
        """Creating a circle

        Args:
            radius (Union[float, int]): radius of a circle

        Raises:
            Exception: check for a negative number
            Exception: data format check
        """
        if radius <= 0:
            raise Exception("Такую окружность не построить")
        if not isinstance(radius, Union[float, int]):
            raise Exception("Неверный формат данных")
        self.__radius = radius

    @property
    def radius(self):
        """getter for radius"""
        return self.__radius

    @radius.setter
    def radius(self, radius: Union[float, int]):
        """setter for radius

        Args:
            radius (Union[float, int]): radius of a circle

        Raises:
            Exception: check for a negative number
            Exception: data format check
        """
        if radius <= 0:
            raise Exception("Такую окружность не построить")
        if not isinstance(radius, Union[float, int]):
            raise Exception("Неверный формат данных")
        self.__radius = radius

    def circumference(self):
        """circle length calculation

        Returns:
            float: circle length
        """
        return round((2 * pi * self.__radius), 2)

    def square(self):
        """circle area calculation

        Returns:
            float: circle area
        """
        return round((pi * self.__radius ** 2), 2)
