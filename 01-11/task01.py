"""File with figure classes."""
from math import pi


class Triangle:
    """The representation of triangle."""

    def __init__(self, side1: float, side2: float, side3: float):
        """Initialization method.

        Args:
            side1 (float): the first side of the triangle.
            side2 (float): the second side of the triangle.
            side3 (float): the third side of the triangle.
        """
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        """Finding the perimeter of the triangle."""
        res = self.side1 + self.side2 + self.side3
        return round(res, 2)

    def area(self):
        """Finding the area of the triangle."""
        s_per = self.perimeter() / 2
        res = (s_per * (s_per - self.side1) * (s_per - self.side2) * (s_per - self.side3)) ** 0.5
        return round(res, 2)


class Circle:
    """The representation of circle."""

    def __init__(self, radius: float):
        """Initialization method.

        Args:
            radius (float): the radius of the circle.
        """
        self.radius = radius

    def length(self):
        """Finding the length of the circle."""
        res = self.radius * pi * 2
        return round(res, 2)

    def area(self):
        """Finding the area of the circle."""
        res = (self.radius ** 2) * pi
        return round(res, 2)
