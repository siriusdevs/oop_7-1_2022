"""File with some classes."""
from math import sqrt, pi


class Triangle:
    """This is representation of triangle."""

    def __init__(self, side1: float, side2: float, side3: float) -> None:
        """Initialization function.

        Args:
            side1 (float): first side of triangle.
            side2 (float): second side of triangle.
            side3 (float): third side of triangle.
        """
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimetr(self) -> float:
        """Count perimetr.

        Returns:
            float: perimetr of triangle.
        """
        return self.side1 + self.side2 + self.side3

    def square(self) -> float:
        """Count square.

        Returns:
            float: square of triangle.
        """
        half_p = self.perimetr() / 2
        return sqrt(half_p * (half_p - self.side1) * (half_p - self.side2) * (half_p - self.side3))


class Circle:
    """This is representation of circle."""

    def __init__(self, radius: float) -> None:
        """Initalization finction.

        Args:
            radius (float): circle's radius.
        """
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
