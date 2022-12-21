"""Representation of a building and a map."""
from additional_functions.json_func import read_json


class InvalidAttribute(Exception):
    """Exception raised for invalid attributes of building."""

    def __init__(self, message: str) -> None:
        """Error initialization.

        Parameters:
            message : str - output message of the error
        """
        self.message = message

    def __str__(self) -> str:
        """Return formated error message."""
        return 'InvalidAttribute: {0}'.format(self.message)


class Building:
    """Representation of a building.

    Attributes:
            height : int - height of the building in meters
            area : int - base area of the building in square meters
            floors : int - number of the floors in the building
            location : tuple - coordinates of the building on the map

    """

    def __init__(self, height: int, area: int, floors: int, location: list = None) -> None:
        """Initialize a building.

        Parameters:
            height : int - height of the building in meters
            area : int - base area of the building in square meters
            floors : int - number of the floors in the building
            location : list - coordinates of the building on the map

        Raises:
            InvalidAttribute: if height, area and floors are not integer
        """
        self.height = height
        self.area = area
        self.floors = floors
        self.location = location
        if not self.is_valid():
            raise InvalidAttribute("Height, area and floors must be integers > 0.")

    def is_valid(self) -> bool:
        """Checks whether a building is valid ot not."""
        attrs = [self.height, self.area, self.floors]
        if all((isinstance(attr, int) for attr in attrs)):
            return all(attr > 0 for attr in attrs)
        return False

    @classmethod
    def from_dict(cls, **kwargs) -> object:
        """Make an object with given kwargs."""
        return cls(**kwargs)

    def to_dict(self) -> dict:
        """Return dictionary of attributes."""
        return self.__dict__

    def __str__(self):
        """String representation of a building."""
        attrs = [self.height, self.area, self.floors, self.location]
        return 'Height: {0}, area: {1}, floors: {2}\nLocation: {3}'.format(*attrs)


class Map:
    """Representation of a map.

    Attributes:
            length : int - lenght of a map
            width : int - widht of a map
            buildings : dict - dictionary of current buildings on the map
    """

    def __init__(self, length: int, width: int, buildings: dict = None) -> None:
        """Initialize a map.

        Parameters:
            length : int - lenght of a map
            width : int - widht of a map
            buildings : dict - dictionary of current buildings on the map

        Raises:
            InvalidAttribute: if length and width are not integers > 0
        """
        self.length = length
        self.width = width
        self.buildings = buildings if buildings else {}
        if not self.is_valid():
            raise InvalidAttribute('Length and width must be integers > 0.')

    def is_valid(self) -> bool:
        """Checks whether the map is valid or not."""
        attrs = [self.length, self.width]
        if all((isinstance(attr, int) for attr in attrs)):
            return all([attr > 0 for attr in attrs])

    @classmethod
    def from_dict(cls, **kwargs) -> object:
        """Make an object with given kwargs."""
        return cls(**kwargs)

    def to_dict(self) -> dict:
        """Return dictionary of attributes."""
        return self.__dict__

    def __str__(self) -> str:
        """String representation of a map."""
        all_buildings = []
        occupied = []
        if self.buildings:
            for name, building_json in self.buildings.items():
                building = Building(**read_json(building_json))
                all_buildings.append('{0}:\n{1}'.format(name, str(building)))
                occupied.append(building.location)
        final_buildings = '\n'.join(all_buildings)
        map_list = [[0] * self.width for _ in range(self.length)]
        while occupied:
            row, col = occupied.pop()
            map_list[row][col] = 1
        full_map = '\n'.join([str(line) for line in map_list])
        all_parameters = [self.length, self.width, full_map, final_buildings]
        return 'Scale: {0}x{1}\n{2}\nBuildings on map:\n{3}'.format(*all_parameters)
