from exeptions_for_triangle import TriangleInvalidSides
import math


class Triangle:
    """
    This class create triangle. / Данный класс создаёт треугольник.
    """

    def __init__(self, a: float or int, b: float or int, c: float or int) -> None:
        """
        This method creates a triangle. /
        Этот метод создаёт треугольник.
        Args:
            a: float First side. / десятичное число - Первая сторона.
            b: float Second side. / десятичное число - Вторая сторона.
            c: float Third side. / десятичное число - Третья сторона.
        Raises:
            ValueError: if any of the sides is not float or int or <= 0. /
            Если любая сторона не десятичная или не целочисленная или меньше или равна 0.
            InvalidTriangleSides: if triangle can't exist. /
            Если такой треугольник не существует.
        """
        if not isinstance(a, (float, int)) or not isinstance(b, (float, int)) \
                or not isinstance(c, (float, int)):
            raise ValueError("Sides must be float or int / Стороны должны быть целочисленные или десятичные")
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Sides must be not zero / Стороны не должны быть нулевыми")
        if Triangle.validation_triangle(a, b, c):
            self.__a = float(a)
            self.__b = float(b)
            self.__c = float(c)
        else:
            raise TriangleInvalidSides([a, b, c])

    @classmethod
    def validation_triangle(cls, a: float or int, b: float or int, c: float or int) -> bool:
        """
        This method checks if such a triangle exists. /
        Этот метод проверяет существует-ли такой треугольник.
        Args:
            a: float First side. / десятичное число - Первая сторона.
            b: float Second side. / десятичное число - Вторая сторона.
            c: float Third side. / десятичное число - Третья сторона.
        Return:
            bool: if triangle is exist or ist exist / логический - когда треугольник существует или нет
        """
        return a + b > c and a + c > b and b + c > a

    @property
    def a(self) -> float:
        """
        Get current value of side a. \
        Возвращает настоящее значение стороны a.
        Returns:
            float - current value of side a. / десятичное число - настоящее значение стороны a.
        """
        return self.__a

    @a.setter
    def a(self, new_a: float or int) -> None:
        """
        Sets a new side a.
        Устанавливает новую сторону а.
        Args:
            new_a: float - current value of side a. / десятичное число - новое значение стороны a.
        """
        if not isinstance(new_a, (float, int)):
            raise ValueError("Side must be float or int / Сторона должна быть целочисленной или десятичной")
        if new_a >= 0:
            raise ValueError("Side must be not zero / Сторона не должна быть нулевой")
        if not Triangle.validation_triangle(new_a, self.__b, self.__c):
            self.__a = new_a
        else:
            raise TriangleInvalidSides([new_a, self.__b, self.__c])

    @property
    def b(self) -> float:
        """
        Get current value of side b.
        Возвращает настоящее значение стороны b.
        Returns:
            float - current value of side b. / десятичное число - настоящее значение стороны b.
        """
        return self.__b

    @b.setter
    def b(self, new_b: float or int) -> None:
        """
        Sets a new side b.
        Устанавливает новую сторону b.
        Args:
            new_b: float - current value of side b. / десятичное число - новое значение стороны b.
        """
        if not isinstance(new_b, (float, int)):
            raise ValueError("Side must be float or int / Сторона должна быть целочисленной или десятичной")
        if new_b >= 0:
            raise ValueError("Side must be not zero / Сторона не должна быть нулевой")
        if not self.validation_triangle(self.__a, new_b, self.__c):
            self.__b = new_b
        else:
            raise TriangleInvalidSides([self.__a, new_b, self.__c])

    @property
    def c(self) -> float:
        """
        Get current value of side с.
        Возвращает настоящее значение стороны с.
        Returns:
            float - current value of side с. / десятичное число - настоящее значение стороны с.
        """
        return self.__c

    @c.setter
    def c(self, new_c: float or int) -> None:
        """
        Sets a new side c.
        Устанавливает новую сторону c.
        Args:
            new_c: float - current value of side c. / десятичное число - новое значение стороны c.
        """
        if not isinstance(new_c, (float, int)):
            raise ValueError("Side must be float or int / Сторона должна быть целочисленной или десятичной")
        if new_c >= 0:
            raise ValueError("Side must be not zero / Сторона не должна быть нулевой")
        if not self.validation_triangle(self.__a, self.__b, new_c):
            self.__c = new_c
        else:
            raise TriangleInvalidSides([self.__a, self.__b, new_c])

    def get_perimeter(self) -> float:
        """
        Counts the perimeter of the current triangle.
        Считает периметр треугольника.
        Returns:
            float - perimeter of the triangle. / десятичное число - периметр треугольника.
        """
        return self.__a + self.__b + self.__c

    def get_square(self) -> float:
        """
        Counts and rounds to 2 decimal places the square of the triangle.
        Считает и округляет до 2-х точек после запятой площадь треугольника
        Returns:
            float - square of the triangle. / десятичное число - площадь треугольника
        """
        half_perimetr = self.get_perimeter() / 2
        square = math.sqrt(half_perimetr * (half_perimetr - self.__a) * \
                           (half_perimetr - self.__b) * (half_perimetr - self.__c))
        return round(square, 2)
