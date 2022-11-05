"""File with classes Triangle and Round."""

import math


class Triangle:
    """Class finds square and perimeter of triangle."""

    def __init__(self, first: int, second: int, third: int) -> None:
        """Method gets three args."""
        self.first = first
        self.second = second
        self.third = third

    def perimeter(self):
        """Method evaluates perimeter.

        Returns:
            int: int - math result rounds up to 2 numbers after dot(sum of sides).
        """
        return self.first + self.second + self.third

    def square(self):
        """Method evaluates square.

        Returns:
            float: float - math result rounds up to 2 numbers after dot(Heron's formula).
        """
        half = (self.first + self.second + self.third) / 2
        return round((half * (half - self.first) * (half - self.second) * (half - self.third)) ** 0.5, 2)


class Circle:
    """Class finds square and perimeter of round."""

    def __init__(self, radius: int) -> None:
        """Method gets one arg."""
        self.radius = radius
        if self.radius <= 0:
            return None

    def length(self):
        """Method which finds length.

        Returns:
            float: float - math result rounds up to 2 numbers after dot(length).
        """
        return round(2 * math.pi * self.radius, 2)

    def square(self):
        """Method which finds round square.

        Returns:
            float: float - math result rounds up to 2 numbers after dot(square).
        """
        return round(math.pi * (self.radius ** 2), 2)
