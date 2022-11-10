"""A few exceptions."""


class InvalidTriangleSides(Exception):
    """Exception for unreal triangles."""

    def __init__(self, sides: list) -> None:
        """Creates a custom exception.

        Args:
            sides: list - list of sides of a triangle
        """
        super().__init__("Triangle with sides: {0}, {1}, {2} - can't exist".format(*sides))


class InvalidCircleRadius(Exception):
    """Exception for unreal circles."""

    def __init__(self, radius: float) -> None:
        """Creates a custom exception.

        Args:
            radius: float - circle's radius
        """
        super().__init__("Circle with radius = {0} - can't exist".format(radius))
