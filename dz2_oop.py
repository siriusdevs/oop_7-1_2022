"""File with some classes."""
from math import sqrt, pi


class NotValidFigure(Exception):
    """This is representation of not valid circle."""

    def __init__(self, sides: list) -> None:
        """Initialization method.

        Args:
            sides (list): sides not valid figure.
        """
        super().__init__(sides)
        self.sides = sides

    def __str__(self) -> None:
        """Exception in special format."""

        return 'Can\'t create figure with sides: {0}'.format(self.sides)


class Triangle:
    """This is representation of triangle."""

    def __init__(self, side1: float, side2: float, side3: float) -> None:
        """Initialization method.If this triangle doesn't exist raises error.

        Args:
            side1 (float): first side of triangle.
            side2 (float): second side of triangle.
            side3 (float): third side of triangle.
        Raises:
            NotValidFigure : if the figure is impossible to build.
        """
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        if not self.is_valid():
            raise NotValidFigure('sides:'[self.side1, self.side2, self.side3])

    def perimeter(self) -> float:
        """Counts perimeter.Rounds it to the 2nd digit after point.

        Returns:
            float: perimeter of triangle.
        """
        return round(self.side1 + self.side2 + self.side3, 2)

    def square(self) -> float:
        """Count square.Round it to the 2th digit after point.
        
        Returns:
            float: square of triangle.
        """
        half_p = self.perimeter() / 2
        return round(sqrt(half_p * (half_p - self.side1) * (half_p - self.side2) * (half_p - self.side3)), 2)

    def is_valid(self) -> bool:
        """Check triangle.

        Returns:
            bool: True if this triangle exists else False.
        """
        sides = [self.side1, self.side2, self.side3]
        for side in sides:
            if not isinstance(side, (int, float)):
                return False
            if side <= 0:
                return False
        sides.sort()
        return sides[2] < sides[0] + sides[1]


class Circle:
    """This is representation of circle."""

    def __init__(self, radius: float) -> None:
        """Initalization method.If this circle doesn't exists raise error.

        Args:
            radius (float): circle's radius.
        Raises:
            NotValidFigure : if the figure is impossible to build.
        """
        self.radius = radius
        if not self.is_valid():
            raise NotValidFigure('radius:'[self.radius])

    def length(self) -> float:
        """Count length.Round it to the 2th digit after point.

        Returns:
            float: circle's length.
        """
        return round(2 * pi * self.radius, 2)

    def square(self) -> float:
        """Count square.Round it to the 2th digit after point.

        Returns:
            float: circle's square.
        """
        return round(pi * (self.radius**2), 2)

    def is_valid(self) -> bool:
        """Check circle.

        Returns:
            bool: True if this circle exists else False.
        """
        if not isinstance(self.radius, (int, float)):
            return False
        elif self.radius <= 0:
            return False
        return True
    