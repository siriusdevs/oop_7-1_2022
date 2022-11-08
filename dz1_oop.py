"""File with some classes."""
import math


class Triangle():
    """This is representation of triangle."""

    def __init__(self, side1: int, side2: int, side3: int) -> None:
        """Initialization method.

        Args:
            side1 (int): first side of triangle.
            side2 (int): second side of triangle.
            side3 (int): third side of triangle.
        """        
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self) -> int:
        """Count perimeter.Round it to the 5th digit after point.

        Returns:
            int: perimeter of triangle.
        """        
        perim = self.side1 + self.side2 + self.side3
        return perim

    def square(self) -> float:
        """Count square.

        Returns:
            float: square of triangle.
        """        
        perimetr = self.perimeter()
        squar = round((perimetr * (perimetr - self.side1) * (perimetr - self.side2) * (perimetr - self.side3))**0.5, 2)
        return squar

class Circle():
    """This is representation of circle."""

    def __init__(self, radius: int) -> None:
        """Initalization method.

        Args:
            r (int): circle's radius.
        """        
        self.radius = radius

    def square(self) -> float:
        """Count length.

        Returns:
            float: circle's square.
        """        
        radiu = self.radius
        s = round(math.pi * radiu * radiu, 2)
        return s

    def length(self) -> None:
        """Count length.

        Returns:
            _type_: circle's length.
        """        
        radiu = self.radius
        lengt = round(math.pi * 2 * radiu, 2)
        return lengt
