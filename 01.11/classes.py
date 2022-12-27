"""Два класса - треугольник и круг, вспомогательный класс - ошибка."""
import math


class NotValidArgs(Exception):
    """вспомогательный класс - ошибка aргументов."""

    pass


class Triangle:
    """Класс треугольника для вычисления периметра и площади."""

    def __init__(self, a, b, c):
        """Принятие трёх сторон.

        Args:
            a(float): первая сторона
            b(float): вторая сторона
            c(float): третья сторона

        Raises:
            NotValidArgs: вызываемая ошибка при неправильных аргументах
        """
        self.a = a
        self.b = b
        self.c = c
        if not self.is_valid():
            raise NotValidArgs("Triangle's sides error")

    def is_valid(self):
        """Проверка треугольника на возможность существования."""
        for side in (self.a, self.b, self.c):
            if not isinstance(side, (int, float)):
                return False
        return max(self.a, self.b, self.c) < (self.a + self.b + self.c - max(self.a, self.b, self.c))

    def perimeter(self):
        """Вычисление периметра c округлением до 3 знаков после запятой."""
        return round(self.a + self.b + self.c, 3)

    def area(self):
        """Вычисление площади c округлением до 3 знаков после запятой."""
        p = self.perimeter() / 2
        return round((p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5, 3)


class Circle:
    """Класс круга для вычисления площади круга и длины окружности."""

    def __init__(self, r):
        """Принятие радиуса круга.

        Args:
            r(float): радиус

        Raises:
            NotValidArgs: вызываемая ошибка при неправильных аргументах
        """
        self.r = r
        if not self.is_valid():
            raise NotValidArgs("Circle's radius error")

    def is_valid(self):
        """Проверка круга на возможность существования."""
        if isinstance(self.r, (int, float)):
            if self.r > 0:
                return True
        return False

    def length(self):
        """Вычисление длины окружности c округлением до 3 знаков после запятой."""
        return round(2 * self.r * math.pi, 3)

    def area(self):
        """Вычисление площади круга c округлением до 3 знаков после запятой."""
        return round(math.pi * self.r ** 2, 3)
