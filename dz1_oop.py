"""File with some classes."""
import math


class Triangle():
    """This is representation of triangle."""

    def __init__(self, side1: int, side2: int, side3: int) -> None:
        """Initialization method.

        Args:
            side1 (int): first side of triangle.
            side2 (int): second side of triangle.
            side3 (int): third side of triangle.
        """
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self) -> float:
        """Count perimeter.Round it to the 5th digit after point.

        Returns:
            float: perimeter of triangle.
        """
        return self.side1 + self.side2 + self.side3

    def square(self) -> float:
        """Count square. Round it to the 2th digit after point.

        Returns:
            float: square of triangle.
        """
        prmtr = self.perimeter()
        return round((prmtr * (prmtr - self.side1) * (prmtr - self.side2) * (prmtr - self.side3))**0.5, 2)


class Circle():
    """This is representation of circle."""

    def __init__(self, radius: float) -> None:
        """Initalization method.

        Args:
            radius (float): circle's radius.
        """
        self.radius = radius

    def square(self) -> float:
        """Count length. Round it to the 2th digit after point.

        Returns:
            float: circle's square.
        """
        return round(math.pi * self.radius * self.radius, 2)

    def length(self) -> float:
        """Count length. Round it to the 2th digit after point.

        Returns:
            float: circle's length.
        """
        return round(math.pi * 2 * self.radius, 2)
