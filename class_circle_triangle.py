"""Find the area and the length of circle."""

import math
from typing import List


class NotValidAttributesError(Exception):
    """Exception raised for invalid sides of triangle or radius of circle."""

    def __init__(self, message: str):
        """Error initialization.

        Parameters:
            message(str): output message of the error
        """
        self.message = message

    def __str__(self):
        """Return formated error message."""
        return 'NotValidAttributesError: {0}'.format(self.message)


class Circle:
    """Class Circle.

    Attributes:
    radius(float): radius of the circle
    """

    def __init__(self, radius: float) -> None:
        """Initialization method.

        Args:
            radius(float): radius of circle

        Raises:
            NotValidAttributesError: if radius is invalid
        """
        self.radius = radius
        if not self.is_valid():
            raise NotValidAttributesError('Circle cannot be built with this radius')

    def length_of_circle(self) -> float:
        """Method that counts the length of circle. Rounds it to 2 decimal places.

        Returns:
            float: the length of circle
        """
        return round(2 * math.pi * self.radius, 2)

    def area(self) -> float:
        """Method that counts the area of circle. Rounds it to 2 decimal places.

        Returns:
            float: area of circle
        """
        return round(math.pi * self.radius ** 2, 2)

    def is_valid(self):
        """Checks condition of circle`s existence."""
        if not isinstance(self.radius, (int, float)):
            return False
        elif self.radius <= 0:
            return False
        return True


class Triangle:
    """Class Triangle."""

    def __init__(self, sides: List[float]):
        """Initialization method.

        Args:
            sides(List[float]): list of sides of the triangle

        Raises:
            NotValidAttributesError: if sides of the triangle are invalid
        """
        self.sides = sides
        if not self.is_valid():
            raise NotValidAttributesError('Triangle cannot be built with these sides')

    def perimeter(self):
        """Counts the perimeter of circle.

        Returns:
            float: the perimeter of circle
        """
        return sum(self.sides)

    def area(self):
        """Counts the area of circle. Rounds it to 2 decimal places.

        Returns:
            float: the area of circle
        """
        p = self.perimeter() / 2
        area_2 = p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2])
        return round(area_2 ** 0.5, 2)

    def is_valid(self):
        """Checks condition of circle`s existence."""
        for side in self.sides:
            if not isinstance(side, (int, float)) and side <= 0:
                return False
        std = sorted(self.sides)
        if std[-1] >= std[0] + std[1]:
            return False
        return True
