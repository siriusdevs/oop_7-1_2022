"""File with some classes of figures."""
from math import sqrt, pi


class Triangle:
    """Representation of the triangle.

    Attributes:
        side1 : int - first side of the triangle
        side2 : int - second side of the triangle
        side3 : int - third side of the triangle
    """

    def __init__(self, side1: int, side2: int, side3: int) -> None:
        """Initialize triangle.

        Parameters:
            side1 : int - first side of the triangle
            side2 : int - second side of the triangle
            side3 : int - third side of the triangle
        """
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self) -> int:
        """Evaluate perimeter of the triangle using Heron's formula."""
        return self.side1 + self.side2 + self.side3

    def area(self) -> float:
        """Evaluate area of the triangle and round the number to 2 decimal places."""
        semi_p = self.perimeter() / 2
        return round(sqrt(semi_p * (semi_p - self.side1) * (semi_p - self.side2) * (semi_p - self.side3)), 2)


class Circle:
    """Representation of the circle.

    Attributes:
        radius : int - radius of the circle
    """

    def __init__(self, radius: int) -> None:
        """
        Initialize circle.

        Parameters:
            radius : int - radius of the circle
        """
        self.radius = radius

    def length(self) -> float:
        """Evaluate length of the circle and round the number to 2 decimal places."""
        return round(2 * pi * self.radius, 2)

    def area(self) -> float:
        """Evaluate area of the circle and round the number to 2 decimal places."""
        return round(pi * (self.radius ** 2), 2)
