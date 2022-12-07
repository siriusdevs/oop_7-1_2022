"""the figure function"""
import math


class Triangle:
    """This is triangle perimetr and area."""

    def __init__(self, a_side: float, b_side: float, c_side: float) -> None:
        """Initialization method.

        Args:
            a_side(float): first side of triangle
            b_side(float): second side of triangle
            c_side(float): third side of triangle
        """
        self.a_side = a_side
        self.b_side = b_side
        self.c_side = c_side

    def perimetr(self) -> None:
        """The perimetr of triangle.

        Returns:
            perimetr(float).
        """
        return self.a_side + self.b_side + self.c_side

    def area(self) -> None:
        """The area of triangle

        Returns:
            area(foat).
        """
        pol = (self.a_side + self.b_side + self.c_side) / 2
        squ = math.sqrt(pol * (pol - self.a_side) * (pol - self.b_side) * (pol - self.c_side))
        return squ


class Circle:
    """This is area and length(perimetr) of circle."""

    def __init__(self, radius: float) -> None:
        """Initialization method.

        Args:
            radius(float): radius of circle.
        """
        self.radius = radius

    def area_circle(self) -> None:
        """The area of circle.

        Returns:
            area(float).
        """
        return round(math.pi * (self.radius**2), 1)

    def perimetr_circle(self) -> None:
        """The length(perimetr) of circle.

        Returns:
            perimetr(float): length of circle.
        """
        return round(2 * math.pi * self.radius, 1)


triangle = Triangle(6, 12, 10)
circle = Circle(3)


print("Площадь круга", round(circle.area_circle(), 1))
print("Длина окружности", round(circle.perimetr_circle(), 1))
print("Периметр треугольника", triangle.perimetr())
print("Площадь треугольника", round(triangle.area(), 1))
