"""Find the area and the length of circle."""

import math


class Circle:
    """Class Circle."""

    def __init__(self, radius: float) -> None:
        """Initialization method.

        Args:
            radius(float): radius of circle
        """
        self.radius = radius

    def length_of_circle(self) -> float:
        """Method that counts the length of circle. Rounds the result to the second digit after point.

        Returns:
            float: the length of circle
        """
        return round(2 * math.pi * self.radius, 2)

    def area(self) -> float:
        """Method that counts the area of circle. Rounds the result to the second digit after point.

        Returns:
            float: area of circle
        """
        return round(math.pi * self.radius ** 2, 2)


circle = Circle(3)
