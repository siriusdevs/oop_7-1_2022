"""File with classes Triangle and Round."""

import math


class Triangle:
    """Class finds square and perimeter of triangle.

    Args:
        first: int - first side.
        second: int - second side.
        third: int - third side.
    """

    def __init__(self, first, second, third):
        """Method gets three args.

        Args:
            first: int - method init first side.
            second: int - method init second side.
            third: int - method init third side.
        """
        self.first = first
        self.second = second
        self.third = third

    def perimeter(self):
        """Method counts perimeter.

        Returns:
            int: int - math result(sum of sides).
        """
        return self.first + self.second + self.third

    def square(self):
        """Method counts square.

        Returns:
            float: float - math result(Heron's formula).
        """
        half = (self.first + self.second + self.third) / 2
        return round((half * (half - self.first) * (half - self.second) * (half - self.third)) ** 0.5, 2)


class Round:
    """Class finds square and perimeter of round.

    Args:
        radius: int - radius for square and length.
    """

    def __init__(self, radius):
        """Method gets one arg.

        Args:
            radius: int - radius.
        """
        self.radius = radius

    def length(self):
        """Method which finds length.

        Returns:
            float: float - math result(length).
        """
        if self.radius <= 0:
            return None
        return round(2 * math.pi * self.radius, 2)

    def square(self):
        """Method which finds round square.

        Returns:
            float: float - math result(square)
        """
        if self.radius <= 0:
            return None
        return round(math.pi * (self.radius ** 2), 2)
