"""File with triangle class and circle class."""
import math
from typing import List


class NonexistentFigure(Exception):
    """This error means that the figure does not exist."""

    def __init__(self, value_except: any) -> None:
        """This method takes a value of parties and remembers them.

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
        """This method takes a list of parties and remembers them.

        Arguments:
            sides (List(float)): sides of trinagle.
        Raises:
            NonexistentFigure: if the figure cannot exist.
        """
        self.sides = sides
        if self.isvalid():
            self.side_1 = sides[0]
            self.side_2 = sides[1]
            self.side_3 = sides[2]
        else:
            raise NonexistentFigure(sides)

    def perimeter(self) -> float:
        """Calculates the perimeter and rounds it to thousandths.

        Returns:
            float: the perimeter of the triangle.
        """
        return round(self.side_1 + self.side_2 + self.side_3, 3)

    def area(self) -> float:
        """Calculates the area and rounds it to thousandths.

        Returns:
            float: the area of triangle.
        """
        semi = self.perimeter() * 0.5
        return round((semi * (semi - self.side_1) * (semi - self.side_2) * (semi - self.side_3)) ** 0.5, 3)

    def isvalid(self) -> bool:
        """Checks the triangle.

        returns:
           bool: True if this triangle exists, False otherwise.
        """
        sd = self.sides
        val_type = (int, float)
        if len(sd) == 3:
            if isinstance(sd[0], val_type) and isinstance(sd[1], val_type) and isinstance(sd[2], val_type):
                sides = sorted(sd)
                if sides[0] + sides[1] > sides[2]:
                    return sides[0] > 0 and sides[1] > 0 and sides[2] > 0
                else:
                    print("С сторонами такой длины треугольника не существует!")
                    return False
            else:
                print("Сторонами треугольника должны быть числа!")
                return False
        else:
            print("У треугольника три угла!")
            return False


class Circle:
    """This is a representation of a circle."""

    def __init__(self, radius: float) -> None:
        """This method takes a value of parties and remembers them.

        Args:
            radius (float): circle's radius.
        Raises:
            NoneExistentFigure: if the figure cannot exist
        """
        self.radius = radius
        if not self.isvalid():
            raise NonexistentFigure(radius)

    def circumference(self) -> float:
        """This method calculates the circumference.

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
        valid_type = (int, float)
        if isinstance(self.radius, valid_type):
            return self.radius > 0
        else:
            print("Радиус должен быть числом!")
            return False
