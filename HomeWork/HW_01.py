"""File with triangle class and circle class."""
import math
from typing import List

class Triangle:
    """This is a projection of a triangle."""

    def __init__(self, sides: List[float]) -> None:
        """Initialization method.

        Arguments:
            side1 (float): the first side of the triangle.
            side2 (float): the second side of the triangle.
            side3 (float): third side of the triangle.
        Raises:
            NoneExistentFigure: if the figure cannot exist
        """
        if self.isvalid(sides):
            self.side_1 = sides[0]
            self.side_2 = sides[1]
            self.side_3 = sides[2]
        else:
            raise NoneExistentFigure(sides)
        

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
        p = Triangle([self.side_1, self.side_2, self.side_3]).perimeter()*0.5
        return round((p*(p-self.side_1)*(p-self.side_2)*(p-self.side_3)) ** 0.5, 3)

    def isvalid(self, sides: List[float]) -> bool:
        """Checks the triangle.

        returns:
           bool: True if this triangle exists, False otherwise.
        """
        if len(sides) == 3:
            try:
                sides = sorted(sides)
                if sides[0] + sides[1] > sides[2]: 
                    return sides[0] > 0 and sides[1] > 0 and sides[2] > 0
                else:
                    print("С сторонами такой длины треугольника не существует!")
                    return False
            except TypeError:
                print("Сторонами треугольника должны быть числа!")
                return False
        else:
            print("У треугольника три угла!")
            return False


class Circle:
    """This is a projection of a circle."""

    def __init__(self, radius: float) -> None:
        """Initalization method.

        Args:
            radius (float): circle's radius.
        Raises:
            NoneExistentFigure: if the figure cannot exist
        """
        if self.isvalid(radius):
            self.radius = radius
        else:
            raise NoneExistentFigure(radius)

    def circumference(self) -> float:
        """This method calculates the circumference
        
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
    
    def isvalid(self, radius: float) -> bool:
        """Checks the circle.
        
        returns:
           bool: True if this circle exists, False otherwise.
        """
        try:
            radius = radius * 1
            return radius > 0
        except TypeError:
            print("Радиус должен быть числом!")
            return False


class NoneExistentFigure(Exception):
    """This error means that the figure does not exist"""
    
    def __init__(self, value: any) -> None:
        """Initialization method.
        
        Args:
            value (Any): the value(s) that caused the error.
        """
        super().__init__(value)
        self.value = value

    def __str__(self) -> None:
        """Exception in special format."""

        return "{0} - this value(s) caused an error NoneExistentFigure".format(self.value)

print(Circle(6.0).circumference())