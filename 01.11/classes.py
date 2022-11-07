"""Docstring."""
import math


class Triangle:
    """Класс треугольника для вычисления периметра и площади."""

    def __init__(self, a, b, c):
        """Принятие трёх сторон.

        Args:
            a(float): первая сторона
            b(float): вторая сторона
            c(float): третья сторона
        """
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        """Вычисление периметра."""
        return round(self.a + self.b + self.c, 5)

    def area(self):
        """Вычисление площади."""
        p = self.perimeter() / 2
        return round((p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5, 5)


class Circle:
    """Класс круга для вычисления площади круга и длины окружности."""

    def __init__(self, r):
        """Принятие радиуса круга.

        Args:
            r(float): радиус
        """
        self.r = r

    def length(self):
        """Вычисление длины окружности."""
        return round(2 * self.r * math.pi, 5)

    def area(self):
        """Вычисление площади круга."""
        return round(math.pi * self.r ** 2, 5)


tr1 = Triangle(2, 4, 3)
cir1 = Circle(55.88)
