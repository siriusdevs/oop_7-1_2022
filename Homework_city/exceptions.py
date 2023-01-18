"""This file exist for exceptions for class House and class City."""


class InvalidMapSize(Exception):
    """Mismatch between map parameters and map sizes."""

    def __init__(self):
        """Mismatch between map parameters and map sizes."""
        super().__init__("Map dimensions do not match parameters")


class InvalidRowOrCol(Exception):
    """Wrong coordinates error."""

    def __init__(self):
        """Wrong coordinates error."""
        super().__init__("Invalid coordinates sent")


class InvalidConfigurationsMap(Exception):
    """Invalid map parameters error."""

    def __init__(self):
        """Invalid map parameters error."""
        super().__init__("Incorrect map parameter values")


class InvalidCountOfBuildings(Exception):
    """Incorrect number of buildings error in map parameters."""

    def __init__(self):
        """Incorrect number of buildings error in map parameters."""
        super().__init__("Incorrect number of houses in parameters")


class InvalidBuildingParams(Exception):
    """Invalid building parameters error."""

    def __init__(self):
        """Incorrect number of buildings error in map parameters."""
        super().__init__("Incorrect building parameters")


class InvalidValuesInParamsBuilding(Exception):
    """Value error in building parameters."""

    def __init__(self):
        """Value error in building parameters."""
        super().__init__("Incorrect building parameter values")


class NullHouseError(Exception):
    """Non-existent building error."""

    def __init__(self):
        """Non-existent building error."""
        super().__init__("Unable to return a non-existent building")


class HouseInsertToHouse(Exception):
    """An error that occurs when it is impossible to put a house on a house."""

    def __init__(self):
        """An error that occurs when it is impossible to put a house on a house."""
        super().__init__("There is already a house here, in order to insert a house on the map, \
                        it is necessary that there be an empty cell")


class DeleteNullHouse(Exception):
    """Error when deleting a non-existent house."""

    def __init__(self):
        """Error when deleting a non-existent house."""
        super().__init__("There is no home, there is nothing to delete")


class InvalidHouseParams(Exception):
    """Invalid home settings error."""

    def __init__(self):
        """Invalid home settings error."""
        super().__init__("Params mast be float or int")


class InvalidHouseName(Exception):
    """Building name error."""

    def __init__(self):
        """Building name error."""
        super().__init__("The name must be a string or not an empty string")


class NullHouseParams(Exception):
    """Error at zero building parameters."""

    def __init__(self):
        """Error at zero building parameters."""
        super().__init__("Parameters must not be null")


class NothingToChange(Exception):
    """An error that occurs when calling a function without passing new structure parameters to it."""

    def __init__(self):
        """An error that occurs when calling a function without passing new structure parameters to it."""
        super().__init__("Nothing to change")


class DoesntExistParamsOnMap(Exception):
    """An error that occurs when the main parameters of the map are missing."""

    def __init__(self):
        """An error that occurs when the main parameters of the map are missing."""
        super().__init__("Basic map parameters not found")


class MapFileDoesntExist(Exception):
    """Error that occurs when the map file is missing."""

    def __init__(self):
        """Error that occurs when the map file is missing."""
        super().__init__("Map file not found")
