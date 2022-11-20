"""File with some classes of figures."""
from math import sqrt, pi


class InvalidFigureError(Exception):
    """Exception raised for invalid attributes of figures."""

    def __init__(self, message: str) -> None:
        """Error initialization.

        Parameters:
            message : str - output message of the error
        """
        self.message = message

    def __str__(self) -> str:
        """Return formated error message."""
        return 'InvalidFigureError: {0}'.format(self.message)


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

        Raises:
            InvalidFigureError: if sides are strings, less than zero or do not satisfy existence condition
        """
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        if not self.is_valid():
            raise InvalidFigureError('Triangle can not be built with these sides.')

    def perimeter(self) -> int:
        """Evaluate perimeter of the triangle using Heron's formula."""
        return self.side1 + self.side2 + self.side3

    def area(self) -> float:
        """Evaluate area of the triangle and round the number to 2 decimal places."""
        semi_p = self.perimeter() / 2
        return round(sqrt(semi_p * (semi_p - self.side1) * (semi_p - self.side2) * (semi_p - self.side3)), 2)

    def is_valid(self) -> bool:
        """Check condition of triangle`s existence."""
        sides = [self.side1, self.side2, self.side3]
        for side in sides:
            if not isinstance(side, (int, float)):
                return False
            if side <= 0:
                return False
        sides.sort()
        return sides[2] < sides[0] + sides[1]


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

        Raises:
            InvalidFigureError: if radius is string or less than zero
        """
        self.radius = radius
        if not self.is_valid():
            raise InvalidFigureError('Circle can not be built with this radius.')

    def length(self) -> float:
        """Evaluate length of the circle and round the number to 2 decimal places."""
        return round(2 * pi * self.radius, 2)

    def area(self) -> float:
        """Evaluate area of the circle and round the number to 2 decimal places."""
        return round(pi * (self.radius ** 2), 2)

    def is_valid(self):
        """Check condition of circle`s existence."""
        if not isinstance(self.radius, (int, float)):
            return False
        elif self.radius <= 0:
            return False
        return True
