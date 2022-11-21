"""File with classes Triangle and Circle."""

import math


class Triangle:
    """Class finds square and perimeter of triangle."""

    def __init__(self, first: int, second: int, third: int) -> None:
        """Method which initialize class Triangle.

        Args:
            first: int - init first side.
            second: int - init second side.
            third: int - init third side.

        Raises:
            ValueError: Exception - if sides in allowed values.
        """
        self.first = first
        self.second = second
        self.third = third
        sides_list = [self.first, self.second, self.third]
        if not isinstance(all(sides_list), int | float) or not self.sides_sum_check() or not self.sides_check():
            raise ValueError

    def perimeter(self):
        """Method evaluates triangles perimeter.

        Returns:
            int - math result rounds up to 2 numbers after dot(sum of sides).
        """
        return self.first + self.second + self.third

    def square(self):
        """Method evaluates triangles square.

        Returns:
            float - math result rounds up to 2 numbers after dot(Heron's formula).
        """
        half = (self.first + self.second + self.third) / 2
        return round((half * (half - self.first) * (half - self.second) * (half - self.third)) ** 0.5, 2)

    def sides_sum_check(self):
        """Method checks triangle for existence.

        Returns:
            bool - if sum of 2 sides larger last one.
        """
        side1 = self.first
        side2 = self.second
        side3 = self.third
        return side1 + side2 > side3 and side3 + side1 > side2 and side3 + side2 > side1

    def sides_check(self):
        """Function checks sides for existence.

        Returns:
            bool - if sides larger 0.
        """
        return self.first > 0 and self.second > 0 and self.third > 0


class Circle:
    """Class finds circles square and perimeter."""

    def __init__(self, radius: int) -> None:
        """Method which initialize class Circle.

        Args:
            radius: int - init radius.

        Raises:
            ValueError: Exception - if radius in allowed values.
        """
        self.radius = radius
        if not isinstance(self.radius, int | float) or not self.radius_check():
            raise ValueError

    def length(self):
        """Method which finds circles length.

        Returns:
            length: float - math result rounds up to 2 numbers after dot(length).
        """
        return round(2 * math.pi * self.radius, 2)

    def square(self):
        """Method which finds circles square.

        Returns:
            square: float - math result rounds up to 2 numbers after dot(square).
        """
        return round(math.pi * (self.radius ** 2), 2)

    def radius_check(self):
        """Method checks radius for existence.

        Returns:
            radius_existence: if radius lower or equals 0.
        """
        return self.radius > 0
