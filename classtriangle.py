"""Find the area and the perimeter of triagle."""


class Triangle:
    """Class Triangle."""

    def __init__(self, side1: float, side2: float, side3: float):
        """Initialization method.

        Args:
            side1(float): 1st side of triangle
            side2(float): 2st side of triangle
            side3(float): 3st side of triangle
        """
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        """Method that counts the perimeter of circle.

        Returns:
            float: the perimeter of circle
        """
        return self.side1 + self.side2 + self.side3

    def area(self):
        """Method that counts the area of circle.

        Returns:
            float: the area of circle
        """
        p = self.perimeter() / 2
        area_2 = p * (p - self.side1) * (p - self.side2) * (p - self.side3)
        return area_2 ** 0.5
