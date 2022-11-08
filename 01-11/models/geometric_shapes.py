"""Models of geometric shapes."""
import math
from .exeptions import UnrealTriangleError


class Triangle:
    """Class for the geometric figure triangle."""

    def __init__(self, side_a: float, side_b: float, side_c: float) -> None:
        """Creates a triangle.

        Args:
            side_a: float - first side length.
            side_b: float - second side length.
            side_c: float - third side length.

        Raises:
            UnrealTriangleError: if triangle can't exist.
            ValueError: if some sides not be float
        """
        if not isinstance(side_a, (float, int)) or not isinstance(side_b, (float, int)) \
                or not isinstance(side_c, (float, int)):
            raise ValueError("Sides must be float")
        self.__side_a = float(side_a)
        self.__side_b = float(side_b)
        self.__side_c = float(side_c)
        # проверка треугольника на существование
        if not self.check():
            raise UnrealTriangleError([side_a, side_b, side_c])

    def get_perimeter(self) -> float:
        """Counts the perimeter of the current triangle.

        Returns:
            float - perimeter of the triangle.
        """
        return self.side_a + self.side_b + self.side_c

    def get_square(self) -> float:
        """Counts and rounds to 2 decimal places the square of the triangle.

        Returns:
            float - square of the triangle.
        """
        half_p = self.get_perimeter() / 2
        square = math.sqrt(half_p * (half_p - self.side_a) * (half_p - self.side_b) * (half_p - self.side_c))
        return round(square, 2)

    def check(self) -> bool:
        """Checks the triangle for existence.

        Returns:
            bool - true if the triangle can existence else false.
        """
        side_a, side_b, side_c = self.__side_a, self.__side_b, self.__side_c
        return side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a

    @property
    def side_a(self) -> float:
        """Get current value of sice_a.

        Returns:
            float - current value of side_a.
        """
        return self.__side_a

    @side_a.setter
    def setter_side_a(self, side_a: float) -> None:
        """Setter for side_a.

        Args:
            side_a: float - new value for side_a.

        Raises:
            ValueError : if new value not be numeric.
            UnrealTriangleError : if new triangle can't exist.
        """
        try:
            self.__side_a = float(side_a)
        except ValueError:
            raise ValueError("Side must be float, not {0}".format(type(side_a)))

        if not self.check():
            raise UnrealTriangleError([self.side_a, self.side_b, self.side_c])

    @property
    def side_b(self) -> float:
        """Get current value of sice_b.

        Returns:
            float - current value of side_b.
        """
        return self.__side_b

    @side_b.setter
    def setter_side_b(self, side_b: float) -> None:
        """Setter for side_b.

        Args:
            side_b: float - new value for side_b.

        Raises:
            ValueError : if new value not be numeric.
            UnrealTriangleError :if new triangle can't exist.
        """
        try:
            self.__side_b = float(side_b)
        except ValueError:
            raise ValueError("Side must be float, not {0}".format(type(side_b)))

        if not self.check():
            raise UnrealTriangleError([self.side_a, self.side_b, self.side_c])

    @property
    def side_c(self) -> float:
        """Get current value of sice_c.

        Returns:
            float - current value of side_c.
        """
        return self.__side_c

    @side_c.setter
    def setter_side_c(self, side_c: float) -> None:
        """Setter for side_c.

        Args:
            side_c: float - new value for side_b.

        Raises:
            ValueError : if new value not be numeric.
            UnrealTriangleError :if new triangle can't exist.
        """
        try:
            self.__side_c = float(side_c)
        except ValueError:
            raise ValueError("Side must be float, not {0}".format(type(side_c)))
        if not self.check():
            raise UnrealTriangleError([self.side_a, self.side_b, self.side_c])


class Circle:
    """Class for the geometric figure circle."""

    def __init__(self, radius: float) -> None:
        """Creates a circle.

        Args:
            radius: float - radius of circle.
        """
        self.radius = radius

    def get_len_circle(self) -> float:
        """Counts and rounds to 2 decimal places the circumference of the circle.

        Returns:
            float - circumference of the circle.
        """
        return round(math.pi * 2 * self.radius, 2)

    def get_square(self) -> float:
        """Counts and rounds to 2 decimal places the square of the circle.

        Returns:
            float - square of circle.
        """
        return round(math.pi * self.radius ** 2, 2)
