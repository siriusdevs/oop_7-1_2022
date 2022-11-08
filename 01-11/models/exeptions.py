"""A few exceptions."""


class UnrealTriangleError(Exception):
    """Exception for unreal triangles."""

    def __init__(self, sides: list) -> None:
        """Creates a custom exception.

        Args:
            sides: list - list of sides of a triangle
        """
        super().__init__("Triangle with sides: {0}, {1}, {2} - can't exist".format(*sides))
