"""File with some classes."""
from math import sqrt, pi


class Triangle:
    """This is representation of triangle."""

    def __init__(self, side1: float, side2: float, side3: float) -> None:
        """Initialization method."""
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self) -> float:
        """Count perimeter.Round it to the 5th digit after point.

        Returns:
            float: perimeter of triangle.
        """
        return round(self.side1 + self.side2 + self.side3, 5)

    def square(self) -> float:
        """Count square.

        Returns:
            float: square of triangle.
        """
        half_p = self.perimeter() / 2
        return sqrt(half_p * (half_p - self.side1) * (half_p - self.side2) * (half_p - self.side3))


class Circle:
    """This is representation of circle."""

    def __init__(self, radius: float) -> None:
        """Initalization method."""
        self.radius = radius

    def length(self) -> float:
        """Count length.

        Returns:
            float: circle's length.
        """
        return pi * (self.radius**2)

    def square(self) -> float:
        """Count square.

        Returns:
            float: circle's square.
        """
        return 2 * pi * self.radius
