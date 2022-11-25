"""File contains two class of errors: MapErr and BuildErr, class Map and class Town with metods for working with map."""
import json
import csv
from json import dumps


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
        return all([self.floors > 0, self.width > 0, self.floors > 0])

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
        self.matrix = [0 * length for _ in range(width)]
        if not self.is_valid():
            raise MapErr

    def is_valid(self):
        """Check attributes for obj in class."""
        return self.length > 0 and self.width > 0


class Town:
    """Contains methods for towns."""

    @staticmethod
    def maps():
        """Information about all maps of towns.

        Returns:
            nested list: тames of all towns.
        """
        with open('towns.csv', 'rt') as file:
            csv_in = csv.reader(file)
            return [town for town in csv_in]

    @staticmethod
    def see_map(file_name):
        """Map of a town.

        Returns:
            nested list: map.
        """
        with open(file_name, 'rt') as file:
            return json.load(file)['map']

    @staticmethod
    def add_building(file_name, building: Building):
        with open(file_name, 'rt') as file:
            inf = json.load(file)
        map = inf['map']
        if not all([-len(map) - 1 < building.coord_y - 1 < len(map), -len(map[0]) - 1 < building.coord_x - 1 < len(map[0])]):
            return 'Введеные координаты вне карты'
        inf['map'][building.y - 1][building.x - 1] = building.name
        inf['building_{0}'.format(building.name)] = building.to_dict()
        with open(file_name, 'wt') as file:
            data = dumps(inf)
            file.write(data)

    @staticmethod
    def destroy_building(file_name, building_name):
        with open(file_name, 'rt') as file:
            inf = json.load(file)
        coord_x = inf['building_{0}'.format(building_name)]['x']
        coord_y = inf['building_{0}'.format(building_name)]['y']
        inf[coord_y][coord_x] = 0
        inf['building_{0}'.format(building_name)].pop(building_name)
        with open(file_name, 'wt') as file:
            data = dumps(inf)
            file.write(data)

    @staticmethod
    def create_town(map: Map, file_name: str):
        with open('{0}.json'.format(file_name), 'wt') as file:
            data = dumps({'map': map.matrix})
            file.write(data)

        maps = maps()
        maps.append([file_name])
        with open('towns.csv', 'wt') as file:
            csv_out = csv.writer(file)
            csv_out.writerows(maps)
