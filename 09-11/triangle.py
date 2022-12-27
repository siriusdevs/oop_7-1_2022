"""The file with triangle and circle classes"""
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
            ValueError : not a valid triangle.
        """
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        if not self.is_valid():
            raise ValueError

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
        first_side = self.side_a
        second_side = self.side_b
        third_side = self.side_c
        if all([isinstance(first_side, (float|int)), isinstance(second_side, (float|int))]):
            if isinstance(third_side, (float|int)):
                if first_side > 0 and second_side > 0 and third_side > 0:
                    return first_side + second_side > third_side and second_side + third_side > first_side \
                        and first_side + third_side > second_side
        return False


class Circle:
    """This is circle valid, length and area."""

    def __init__(self, radius: float) -> None:
        """Initialization method.

        Args:
            radius(float): radius of circle.

        Raises:
            ValueError: if radius is not valid.
        """
        self.radius = radius
        if not self.is_valid():
            raise ValueError

    def length(self) -> float:
        """Length(perimetr) of circle.

        Returns:
            length(float): length of circle.
        """
        return round((2 * math.pi * self.radius), 2)

    def area(self) -> float:
        """The area of circle.

        Returns:
            area(float).
        """
        return (round(math.pi * self.radius), 2)

    def is_valid(self) -> bool:
        """Validity check.

        Returns:
            bool: if the circle is correct True else False
        """
        if isinstance(self.radius, float|int):
            return self.radius > 0


triangle = Triangle(2, 2, 2)
print('Perimetr:', triangle.perimetr(), 'Area:', triangle.area())
circle = Circle(5)
print('length:', circle.length(), 'Area:', circle.area())
