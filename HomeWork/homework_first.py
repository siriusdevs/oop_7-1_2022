"""File with triangle class and circle class."""
import math
from typing import List


class NonexistentFigure(Exception):
    """This error means that the figure does not exist."""

    def __init__(self, value_except: any) -> None:
        """This method takes a value of sides and remembers them.

        Args:
            value_except (any): the value(s) that caused the error.
        """
        super().__init__(value_except)
        self.value_except = value_except

    def __str__(self) -> None:
        """Exception in special format."""
        return "{0} - this value(s) caused an error NonexistentFigure".format(self.value_except)


class Triangle:
    """This is a representation of a triangle."""

    def __init__(self, sides: List[float]) -> None:
        """This method takes a list of sides and remembers them.

        Arguments:
            sides (List[float]): sides of trinagle.

        Raises:
            NonexistentFigure: if the figure cannot exist.
        """
        self.sides = sides
        if self.isvalid():
            self.first_side = sides[0]
            self.second_side = sides[1]
            self.third_side = sides[2]
        else:
            raise NonexistentFigure(sides)

    def perimeter(self) -> float:
        """Calculates the perimeter and rounds it to thousandths.

        Returns:
            float: the perimeter of the triangle.
        """
        return round(self.first_side + self.second_side + self.third_side, 3)

    def area(self) -> float:
        """Calculates the area and rounds it to thousandths.

        Returns:
            float: the area of triangle.
        """
        semi = self.perimeter() * 0.5
        return round((semi * (semi - self.first_side) * (semi - self.second_side) * (semi - self.third_side)) ** 0.5, 3)

    def isvalid(self) -> bool:
        """Checks the triangle.

        returns:
           bool: True if this triangle exists, False otherwise.
        """
        sd = self.sides
        val_type = (int, float)
        if len(sd) == 3:
            if all([isinstance(x_val, val_type) for x_val in sd]):
                sides = sorted(sd)
                if sides[0] + sides[1] > sides[2]:
                    return sides[0] > 0 and sides[1] > 0 and sides[2] > 0
        return False


class Circle:
    """This is a representation of a circle."""

    def __init__(self, radius: float) -> None:
        """This method takes a value of parties and remembers them.

        Args:
            radius (float): circle's radius.

        Raises:
            NonexistentFigure: if the figure cannot exist.
        """
        self.radius = radius
        if not self.isvalid():
            raise NonexistentFigure(radius)

    def circumference(self) -> float:
        """This method calculates the circumferenceand and rounds it to thousandths.

        Returns:
            float: circumference
        """
        return round((math.pi * self.radius * 2), 3)

    def area(self) -> float:
        """Calculates the area and rounds it to thousandths.

        Returns:
            float: the area of circle.
        """
        return round((math.pi * (self.radius**2)), 3)

    def isvalid(self) -> bool:
        """Checks the circle.

        returns:
           bool: True if this circle exists, False otherwise.
        """
        if isinstance(self.radius, (int, float)):
            return self.radius > 0
        return False
