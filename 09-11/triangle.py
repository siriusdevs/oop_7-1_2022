"""The figur valid function."""
import math


class Triangle:
    """This is triangle valid, perimetr and area."""

    def __init__(self, side_a: float, side_b: float, side_c: float) -> None:
        """Initialization method.

        Args:
            side_a(float): first side of triangle
            side_b(float): second side of triangle
            side_c(float): third side of triangle

        Raises:
            NotValidTriangle : not a valid triangle.
        """
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        if not self.is_valid():
            raise NotValidTriangle

    def perimetr(self) -> float:
        """The perimetr of triangle.

        Returns:
            perimetr(float).
        """
        return round((self.side_a + self.side_b + self.side_c), 2)

    def area(self) -> float:
        """The area of triangle

        Returns:
            area(foat).
        """
        pol = (self.side_a + self.side_b + self.side_c) / 2
        return round((pol * (pol - self.side_a) * (pol - self.side_b) * (pol - self.side_c)), 2)

    def is_valid(self) -> bool:
        """Validity check.

        Returns:
            bool: if the triangle is correct True else False
        """
        sides = sorted([self.side_a, self.side_b, self.side_c])
        for side in sides:
            if not isinstance(side, float|int):
                return False
            if side <= 0:
                return False
        if sides[0] > sides[1] + sides[2]:
            return False
        return True


class NotValidTriangle(Exception):
    """This is class of not valid triangle."""

    pass


class NotValidCircle(Exception):
    """This is class of not valid circle."""

    pass


class Circle:
    """This is circle valid, length and area."""

    def __init__(self, radius: float) -> None:
        """Initialization method.

        Args:
            radius(float): radius of circle.

        Raises:
            NotValidCircle : not a valid circle.
        """
        self.radius = radius
        if not self.is_valid():
            raise NotValidCircle

    def length(self) -> float:
        """Length(perimetr) of circle.

        Returns:
            length(float): length of circle.
        """
        return round(2 * math.pi * self.radius)

    def area(self) -> float:
        """The area of circle.

        Returns:
            area(float).
        """
        return round(math.pi * self.radius)

    def is_valid(self) -> bool:
        """Validity check.

        Returns:
            bool: if the circle is correct True else False
        """
        if isinstance(self.radius, float|int):
            return self.radius > 0


triangle = Triangle(12, 10, 20)
print('Perimetr:', triangle.perimetr(), 'Area:', triangle.area())
circle = Circle(5)
print('length:', circle.length(), 'Area:', circle.area())
