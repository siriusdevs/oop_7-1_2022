"""Find the area and the length of circle."""

import math
from typing import List


class InvalidAttributesError(Exception):
    """Exception raised for invalid sides of triangle or radius of circle."""

    def __init__(self, message: str):
        """Error initialization.

        Parameters:
            message(str): output message of the error
        """
        self.message = message

    def __str__(self):
        """Return formated error message."""
        return 'InvalidAttributesError: {0}'.format(self.message)


class Circle:
    """Representation of a circle.

    Attributes:
    radius(float): radius of the circle
    """

    def __init__(self, radius: float) -> None:
        """Initialization method.

        Args:
            radius(float): radius of circle

        Raises:
            InvalidAttributesError: if radius is invalid
        """
        self.radius = radius
        if not self.is_valid():
            raise InvalidAttributesError('Circle cannot be built with this radius')

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
        return isinstance(self.radius, (int, float)) and self.radius > 0


class Triangle:
    """Representation of a triangle.

    Attributes:
    sides(List[float]): list of sides of the triangle
    """

    def __init__(self, sides: List[float]):
        """Initialization method.

        Args:
            sides(List[float]): list of sides of the triangle

        Raises:
            InvalidAttributesError: if sides of the triangle are invalid
        """
        self.sides = sides
        if not self.is_valid():
            raise InvalidAttributesError('Triangle cannot be built with these sides')

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
        area_2 = p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]) ** 0.5
        return round(float(area_2), 2)

    def is_valid(self):
        """Checks condition of circle`s existence."""
        if all([isinstance(side, (int, float)) and side > 0 for side in self.sides]):
            std = sorted(self.sides)
            return std[-1] < std[0] + std[1]
