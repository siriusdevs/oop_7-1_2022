"""File with some classes."""
from math import sqrt, pi


class NotValidFigure(Exception):
    """This is representation of not valid figure exception."""

    def __init__(self, sides: object) -> None:
        """Initialization method.

        Args:
            sides (object): objects from Exception.
        """
        super().__init__(sides)
        self.sides = sides

    def __str__(self):
        """Exception in special format."""
        return 'Impossible to build figure with {0}'.format(self.sides)


class Triangle:
    """This is representation of triangle."""

    def __init__(self, side1: float, side2: float, side3: float) -> None:
        """Initialization method.If this triangle doesn't exists raise's error.

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
            raise NotValidFigure('sides: {0}, {1}, {2}.'.format(self.side1, self.side2, self.side3))

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

    def is_valid(self) -> bool:
        """Check triangle.

        Returns:
            bool: True if this triangle exists else False.
        """
        if self.side1 + self.side2 > self.side3:
            if self.side1 + self.side3 > self.side2:
                if self.side2 + self.side3 > self.side1:
                    return True
        return False


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
            raise NotValidFigure('radius: {0}'.format(self.radius))

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

    def is_valid(self) -> bool:
        """Check circle.

        Returns:
            bool: True if this circle exists else False.
        """
        return self.radius > 0
