import json, csv
from json import dumps

class MapErr(Exception):
    pass


class BuildErr(Exception):
    pass


class Building:

    def __init__(self, name: str, height: float, width: float, floors: int, coord_x: int, coord_y: int):
        self.name = name
        self.height = height
        self.width = width
        self.floors = floors
        self.x = coord_x
        self.y = coord_y
        if not self.is_valid():
            raise BuildErr

    def is_valid(self):
        return all([self.floors > 0, self.width > 0, self.floors > 0])
    
    def to_dict(self):
        return self.__dict__


class Map:

    def __init__(self, length, width) -> None:
        self.matrix = [0 * length for _ in range(width)]
        if not self.is_valid():
            raise MapErr
    
    def is_valid(self):
        return self.length > 0 and self.width > 0


class Town:

    @staticmethod
    def maps():
        with open('towns.csv', 'rt') as file:
            csv_in = csv.reader(file)
            return [town for town in csv_in]
    
    @staticmethod
    def see_map(file_name):
        with open(file_name, 'rt') as file:
            return json.load(file)['map']

    @staticmethod
    def add_building(file_name, building : Building):
        with open(file_name, 'rt') as file:
            inf = json.load(file)
        map = inf['map']
        if not all([-len(map) - 1 < building.y - 1 < len(map), -len(map[0]) - 1 < building.x - 1 < len(map[0])]):
            return 'Введеные координаты вне карты'
        inf['map'][building.y - 1][building.x - 1] = building.name
        inf['building_{0}'.format(building.name)] = building.to_dict()
        with open(file_name, 'wt') as file:
            data = dumps(inf)
            file.write(data)

    @classmethod
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

        




