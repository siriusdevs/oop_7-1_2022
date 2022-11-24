"""File with figure classes."""
from math import pi


class BadFigure(Exception):
    """The exception is for invalid attributes of figures."""

    def __init__(self, text: str):
        """Error initialization.

        Args:
            text (str): the message of the error.
        """
        self.text = text

    def __str__(self) -> str:
        """Return error message."""
        return 'BadFigure: {0}'.format(self.text)


class Triangle:
    """The representation of triangle."""

    def __init__(self, side1: float, side2: float, side3: float):
        """Initialization method.

        Args:
            side1 (float): the first side of the triangle.
            side2 (float): the second side of the triangle.
            side3 (float): the third side of the triangle.

        Raises:
            BadFigure: if sides aren't correct; if sides are less than zero.
        """
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        if not self.is_valid():
            raise BadFigure('There is no way to create triangle with provided sides.')

    def perimeter(self):
        """Finding the perimeter of the triangle.

        The result is rounded to two decimal places.
        """
        res = self.side1 + self.side2 + self.side3
        return round(res, 2)

    def area(self):
        """Finding the area of the triangle.

        The result is rounded to two decimal places.
        """
        s_per = self.perimeter() / 2
        res = (s_per * (s_per - self.side1) * (s_per - self.side2) * (s_per - self.side3)) ** 0.5
        return round(res, 2)

    def is_valid(self):
        """Check if the triangle exists or not."""
        side1 = self.side1
        side2 = self.side2
        side3 = self.side3
        sides = [self.side1, self.side2, self.side3]
        for side in sides:
            if not isinstance(side, (int, float)):
                return False
        if side1 > 0 and side2 > 0 and side3 > 0:
            return side1 + side2 > side3 and side3 + side1 > side2 and side3 + side2 > side1
        return False


class Circle:
    """The representation of circle."""

    def __init__(self, radius: float):
        """Initialization method.

        Args:
            radius (float): the radius of the circle.

        Raises:
            BadFigure: if radius is incorrect; if radius is less than zero.
        """
        self.radius = radius
        if not self.is_valid():
            raise BadFigure('There is no way to create circle with provided radius.')

    def length(self):
        """Finding the length of the circle.

        The result is rounded to two decimal places.
        """
        res = self.radius * pi * 2
        return round(res, 2)

    def area(self):
        """Finding the area of the circle.

        The result is rounded to two decimal places.
        """
        res = (self.radius ** 2) * pi
        return round(res, 2)

    def is_valid(self):
        """Check if the circle exists or not."""
        if not isinstance(self.radius, (int, float)):
            return False
        if self.radius > 0:
            return True
