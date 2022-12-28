"""A few exceptions."""


class BuildingError(Exception):
    """Exception for building."""

    def __init__(self, msg: str) -> None:
        """Creates a custom exception.

        Args:
            msg: str - error message.
        """
        super().__init__(msg)

class MapError(Exception):
    """Exception for building."""

    def __init__(self, msg: str) -> None:
        """Creates a custom exception.

        Args:
            msg: str - error message.
        """
        super().__init__(msg)

