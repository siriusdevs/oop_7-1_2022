"""This file for circle class."""
import math


class Circle(object):
    """
    Class for create circle.
    Класс для создания круга.
    """

    def __init__(self, radius: float or int) -> None:
        """
        This function creates a circle.
        Данная функция создаёт круг.
        Args:
            radius: float - radius of circle.
            десятичное число - радиус окружности.
        Raises:
            ValueError: if circle radius is not float or int or <= 0.
            Если радиус окружности не десятичный или не целочисленный или меньше или равен 0.
        """

        if self.validation_circle(radius):
            self._radius = radius

    @classmethod
    def validation_circle(cls, radius: float or int) -> bool:
        """
        This method checks validation the circle.
        Данный метод проверяет правильность круга.
        Args:
            radius: float or int - radius of circle.
            десятичный или целочисленный - радиус круга.
        Returns:
            bool - if circle exist.
        """

        if not isinstance(radius, (float, int)):
            raise ValueError("Radius must be float or int / Радиус должен быть целочисленным или десятичным")
        if radius <= 0:
            raise ValueError(
                "Radius must not be less than or equal to zero. Радиус не должен быть меньше или равен нулю.")
        return True

    @property
    def radius(self) -> float:
        """
        Get current value of circle radius.
        Возвращает настоящее значение радиуса круга.
        Returns:
            float - current of circle radius.
            десятичное число - настоящее значение радиуса круга.
        """

        return self._radius

    @radius.setter
    def radius(self, new_radius: float or int) -> None:
        """
        This function changes the radius of the circle.
        Данная функция изменяет радиус круга.
        Args:
            new_radius: float - new radius of circle.
            десятичное число - новый радиус окружности.
        Raises:
            ValueError: if circle radius is not float or int or <= 0.
            Если новый радиус окружности не десятичный или не целочисленный или меньше или равен 0.
        """

        if self.validation_circle(new_radius):
            self._radius = new_radius

    def get_circle_length(self) -> float:
        """
        This function appears in the circle of a rounded two-digit decimal place.
        Данная функция возвращает длину окружности округлённую до двух знаков после запятой.
        Returns:
            float - length of circle rounded two-digit decimal place.
            десятичное число - длина окружности округлённая до двух знаков после запятой.
        """

        return round(math.pi * 2 * self.radius, 2)

    def get_circle_square(self) -> float:
        """
        This function returns the square of a circle rounded two-digit decimal place.
        Данная функция возвращает площадь окружности округлённую до двух знаков после запятой.
        Returns:
            float - square of circle rounded two-digit decimal place.
            десятичное число - площадь окружности округлённая до двух знаков после запятой.
        """

        return round(math.pi * self.radius ** 2, 2)
