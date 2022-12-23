"""the triangle and circle classes"""
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
            perimetr(float) rounds up to 5 numbers after dot.
        """
        return round((self.a_side + self.b_side + self.c_side), 2)

    def area(self) -> None:
        """The area of triangle

        Returns:
            area(foat) rounds up to 5 numbers after dot.

        """
        pol = (self.a_side + self.b_side + self.c_side) / 2
        return round((pol * (pol - self.a_side) * (pol - self.b_side) * (pol - self.c_side)), 2)


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
            area(float) rounds up to 2 numbers after dot.
        """
        return round(math.pi * (self.radius**2), 2)

    def perimetr_circle(self) -> None:
        """The length(perimetr) of circle.

        Returns:
            perimetr(float): length of circle rounds up to 2 numbers after dot.
        """
        return round(2 * math.pi * self.radius, 2)


triangle = Triangle(14, 12, 18)
circle = Circle(3)


print("Площадь круга", circle.area_circle())
print("Длина окружности", circle.perimetr_circle())
print("Периметр треугольника", triangle.perimetr())
print("Площадь треугольника", triangle.area())
