"""Classes."""

from math import pi, sqrt


class NotValidTriang(Exception):
    """There is no such triangle."""

    def __str__(self):
        """Returns the error text."""
        return "No such triangle exists!"


class Triangle:
    """This class can return diameter, length or area of triangle."""

    def __init__(self, side1: float, side2: float, side3: float) -> None:
        """Triangle initialization. If this circle doesn't exists raise error.

        Args:
            side1 (float): the first side of triangle.
            side2 (float): the second side of triangle.
            side3 (float): the third side of triangle.

        Raises:
            NotValidTriang: if the triangle is impossible to build.
        """
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        if not self.is_valid():
            raise NotValidTriang

    def is_valid(self):
        """Check if such a triangle exists.

        Returns:
            bool: result
        """
        sides = sorted([self.side1, self.side2, self.side3], reverse=True)
        for side in sides:
            if not isinstance(side, (float, int)):
                return False
            if side <= 0:
                return False
        return sides[0] < sides[1] + sides[2]

    def perimeter(self) -> float:
        """Count the perimeter of triangle. Rounds it to the 2nd digit after the dot.

        Returns:
            float: perimeter of triangle.
        """
        return round(self.side1 + self.side2 + self.side3, 2)

    def area(self) -> float:
        """Count the area of triangle. Rounds it to the 2nd digit after the dot.

        Returns:
            float: area of triangle.
        """
        per = self.perimeter() / 2
        return round(sqrt(per * (per - self.side1) * (per - self.side2) * (per - self.side3)), 2)


class NotValidCirc(Exception):
    """There is no such circle."""

    def __str__(self):
        """Returns the error text."""
        return "No such triangle exists!"


class Circle:
    """This class can return diameter, length or area of circle."""

    def __init__(self, radius: float) -> None:
        """Circle initialization. If this circle doesn't exists raise error.

        Args:
            radius (float): the radius of circle.

        Raises:
            NotValidCirc: if the circle is impossible to build.
        """
        self.radius = radius
        if not self.is_valid():
            raise NotValidCirc

    def is_valid(self) -> bool:
        """Check if such a circle exists.

        Returns:
            bool: result
        """
        if not isinstance(self.radius, (float, int)):
            return False
        elif self.radius <= 0:
            return False
        return True

    def diameter(self):
        """Count the diameter of circle. Rounds it to the 2nd digit after the dot.

        Returns:
            float: diameter of circle.
        """
        return 2 * self.radius

    def length(self) -> float:
        """Count the length of circle. Rounds it to the 2nd digit after the dot.

        Returns:
            float: length of circle.
        """
        return round(self.diameter() * pi, 2)

    def area(self) -> float:
        """Count the area or circle. Rounds it to the 2nd digit after the dot.

        Returns:
            float: area of circle.
        """
        return round(pi * self.radius ** 2, 2)
