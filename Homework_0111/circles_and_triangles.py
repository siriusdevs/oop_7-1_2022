"""Classes Circle and Triangle."""
from cmath import pi


class STerr(Exception):
    """Our error for wrong attributes."""

    pass


class Circle:
    """Contains methods for circles."""

    def __init__(self, radius: float):
        """Method which initialize class Circle.

        Args:
            radius: float - radius of a circle.

        Raises:
            STerr: Exception - radius less then 0 or 0
        """
        self.radius = radius
        if not self.is_valid():
            raise STerr

    def is_valid(self):
        """Check attributes for obj in class."""
        if isinstance(self.radius, (int, float)):
            return self.radius > 0
        return False

    def area(self):
        """Area of a circle.

        Returns:
            Area rounded to 3 decimal places.
        """
        return round(self.radius ** 2 * pi, 3)

    def len_of_circle(self):
        """Len of circle.

        Returns:
            Len rounded to 3 decimal places.
        """
        return round(2 * pi * self.radius, 3)


class Triangle:
    """Contains methods for triangles."""

    def __init__(self, first_side: float, second_side: float, third_side: float):
        """Method which initialize class Triangle.

        Args:
            first_side: int - first side of a triangle.
            second_side: int - second side of a triangle.
            third_side: int - third side of a triangle.

        Raises:
            STerr: Exception - any of sides less then 0 or 0
        """
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side
        if not self.is_valid():
            raise STerr

    def is_valid(self):
        """Checks acceptability of an attribute."""
        fir = self.first_side
        sec = self.second_side
        th = self.third_side
        if all(isinstance(fir, (int, float)), isinstance(sec, (int, float))):
            if isinstance(th, (int, float)):
                if fir > 0 and sec > 0 and th > 0:
                    return fir + sec > th and sec + th > fir and fir + th > sec
        return False

    def perimeter(self):
        """Perimeter of a triangle."""
        return self.first_side + self.second_side + self.third_side

    def area(self):
        """Area of a triangle.

        Returns:
            Area rounded to 3 decimal places.
        """
        hp = self.perimeter() / 2
        area = (hp * (hp - self.first_side) * (hp - self.second_side) * (hp - self.third_side)) ** 0.5
        return round(area, 3)
