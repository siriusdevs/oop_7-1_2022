class TriangleInvalidSides(Exception):
    """
    Exception for non-existent triangle.
    Ошибка несуществующего треугольника.
    """

    def __init__(self, sides: list) -> None:
        """
        Exception for create triangle. \
        Ошибка создания треугольника.

        Args:
            sides: list - of sides of a triangle. / список - список со сторонами треугольника.
        """
        super().__init__("Triangle with sides: {0}, {1}, {2} - can't exist / "
                         "Треугольник со сторонами: {0}, {1}, {2} - не существует".format(*sides))
