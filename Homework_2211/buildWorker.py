"""File contains class of errors: MapErr and BuildErr, class Map and class Town with metods for working with map."""
from json import load, dumps
import csv


class MapErr(Exception):
    """Error for wrong matrix dimension."""

    pass


class BuildErr(Exception):
    """Error for wrong attributes of a Building."""

    pass


class Building:
    """Contains methods for buildings."""

    def __init__(self, name: str, height: float, width: float, floors: int, coord_x: int, coord_y: int):
        """Method which initialize class Building.

        Args:
            name: str - name of a building.
            height: float - height of a building.
            width: float - width of a building.
            floors: int - number of floors of a building.
            coord_x: int - coordinate x of a building on the map.
            coord_y: int - coordinate y of a building on the map.

        Raises:
            BuildErr: Exception - Any of the digital attributes is non-positive
        """
        self.name = name
        self.height = height
        self.width = width
        self.floors = floors
        self.coord_x = coord_x
        self.coord_y = coord_y
        if not self.is_valid():
            raise BuildErr

    def is_valid(self) -> bool:
        """Check attributes for obj in class."""
        if all([isinstance(attr, (int, float)) for attr in (self.height, self.width)]):
            if all([isinstance(attr, int) for attr in (self.floors, self.coord_x, self.coord_y)]):
                return all([attr > 0 for attr in (self.floors, self.width, self.height)])
        return False

    def to_dict(self) -> dict:
        """Attributes of an obj in dict.

        Returns:
            dict: attributes.
        """
        return self.__dict__


class Map:
    """Contains methods for maps."""

    def __init__(self, length: int, width: int) -> None:
        """Method which initialize class Map.

        Args:
            length: int - length of a map.
            width: int - width of a map.

        Raises:
            MapErr: Exception - Any of the attributes is non-positive
        """
        self.length = length
        self.width = width
        self.matrix = [[0] * length for _ in range(width)]
        if not self.is_valid():
            raise MapErr

    def is_valid(self) -> bool:
        """Check attributes for obj in class."""
        if all([isinstance(self.length, int), isinstance(self.width, int)]):
            return self.length > 0 and self.width > 0
        return False


class Town:
    """Contains methods for towns."""

    @staticmethod
    def maps():
        """Information about all towns.

        Returns:
            nested list: names of all towns.
        """
        with open('towns.csv', 'rt') as csv_file:
            csv_in = csv.reader(csv_file)
            return [town for town in csv_in]

    @staticmethod
    def see_map(file_name: str):
        """Map of a town.

        Args:
            file_name: str - name of a town (in the same time name of json file).

        Returns:
            nested list: map.
        """
        with open(file_name, 'rt') as json_file:
            return load(json_file)['map']

    @staticmethod
    def see_buildings(file_name: str, coordinates: str):
        """Buildings of a town.

        Args:
            file_name: str - name of a town (in the same time name of json file).
            coordinates: str - building\'s coordinates on the map
        Returns:
            dict: information about a building.
        """
        with open(file_name, 'rt') as json_file:
            inform = load(json_file)
            if coordinates in inform:
                return inform[coordinates]
            else:
                return 'No such a building'

    @staticmethod
    def add_building(file_name: str, building: Building):
        """Function for creation a building. Writes to json file information about building.

        Args:
            file_name: str - name of a town (in the same time name of json file).
            building: Building - obj of class Building for creation in town.
        """
        with open(file_name, 'rt') as json_file:
            inf = load(json_file)
        map = inf['map']
        len_m = len(map)
        if not all([-len_m - 1 < building.coord_y < len_m, -len(map[0]) - 1 < building.coord_x < len(map[0])]):
            print('Entered coordinates outside the map')
            return None
        if not inf['map'][building.coord_y][building.coord_x] == 0:
            print('-' * 100)
            print('There is already a building on this place')
            print('-' * 100)
            return None
        inf['map'][building.coord_y][building.coord_x] = 'X'
        inf[(str(building.coord_y) + str(building.coord_x))] = building.to_dict()
        with open(file_name, 'wt') as json_file:
            dumps_inf = dumps(inf)
            json_file.write(dumps_inf)

    @staticmethod
    def destroy_building(file_name: str, coordinates: str):
        """Function for destroying a building. Removes from json file information about building.

        Args:
            file_name: str - name of a town (in the same time name of json file).
            coordinates: str - building\'s coordinates on the map.
        """
        with open(file_name, 'rt') as json_file:
            inf = load(json_file)
        coord_x = inf[coordinates]['coord_x']
        coord_y = inf[coordinates]['coord_y']
        inf['map'][coord_y][coord_x] = 0
        inf.pop(coordinates)
        with open(file_name, 'wt') as json_file:
            dumps_inf = dumps(inf)
            json_file.write(dumps_inf)

    @staticmethod
    def create_town(map: Map, file_name: str):
        """Function for creation a town. Creates jsonfile with map of new town and wtites to csv file name of the town.

        Args:
            map: Map - map of new town (object of class Map ).
            file_name: str - name of a town (in the same time name of new json file).
        """
        with open('{0}.json'.format(file_name), 'wt') as json_file:
            dumps_map = dumps({'map': map.matrix})
            json_file.write(dumps_map)

        maps = Town.maps()
        maps.append([file_name])
        with open('towns.csv', 'wt') as csv_towns:
            csv_out = csv.writer(csv_towns)
            csv_out.writerows(maps)
