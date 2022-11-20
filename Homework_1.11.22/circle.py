import math


class Circle:
    """Class for create circle. / Класс для создания круга."""
    def __init__(self, radius: float or int) -> None:
        """
        This function creates a circle. / Данная функция создаёт круг.
        Args:
            radius: float - radius of circle. / десятичное число - радиус окружности.
        Raises:
            ValueError: if circle radius is not float or int or <= 0. \
            Если радиус окружности не десятичный или не целочисленный или меньше или равен 0.
        """
        if not isinstance(radius, (float, int)):
            raise ValueError("Radius must be float or int / Радиус должен быть целочисленным или десятичным")
        if radius <= 0:
            raise ValueError("Radius must not be less than or equal to zero. \
             Радиус не должен быть меньше или равен нулю.")
        self.__radius = radius

    @property
    def radius(self) -> float:
        """
        Get current value of circle radius. \
        Возвращает настоящее значение радиуса круга.
        Returns:
            float - current of circle radius. / десятичное число - настоящее значение радиуса круга.
        """
        return self.__radius

    @radius.setter
    def radius(self, new_radius: float or int) -> None:
        """
        This function changes the radius of the circle. / Данная функция изменяет радиус круга.
        Args:
            new_radius: float - new radius of circle. / десятичное число - новый радиус окружности.
        Raises:
            ValueError: if circle radius is not float or int or <= 0. \
            Если новый радиус окружности не десятичный или не целочисленный или меньше или равен 0.
        """
        if not isinstance(new_radius, (float, int)):
            raise ValueError("Radius must be float or int / Радиус должен быть целочисленным или десятичным")
        if new_radius <= 0:
            raise ValueError("Radius must not be less than or equal to zero. \
             Радиус не должен быть меньше или равен нулю.")
        self.__radius = new_radius

    def get_circle_length(self) -> float:
        """
        This function returns the length of a circle. / Данная функция возвращает длину окружности
        Returns:
            float - length of circle. / десятичное число - длина окружности.
        """
        return round(math.pi * 2 * self.radius, 2)

    def get_circle_square(self) -> float:
        """
        This function returns the square of a circle. / Данная функция возвращает площадь окружности
        Returns:
            float - square of circle. / десятичное число - площадь окружности.
        """
        return round(math.pi * self.radius ** 2, 2)
