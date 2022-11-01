"""A little module to remind you how to create classes dynamically."""


def create_class(name: str, obj_data: dict):
    """Creates a class dynamically.

    Args:
        name : str - the name of the class.
        obj_data : dict - methods and attributes of the class.

    Returns:
        class : a class based on given data.
    """
    return type(name, (object,), obj_data)
