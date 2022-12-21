"""File with classes wich is needed in main."""
from typing import Union, List
import numpy as np
import json
import os.path
from time import sleep


class NotExisting(Exception):
    """This is representation of not existing smth."""

    def __init__(self, input_cls: any, parametrs: list,) -> None:
        """Initialization method.

        Args:
            input_cls (any): class of something.
            parametrs (list): parametrs of something.
        """
        super().__init__(parametrs)
        self.input_cls = input_cls
        self.parametrs = parametrs

    def __str__(self) -> str:
        """Exception in special format."""
        return "Impossible to create {0} with parametrs: {1}".format(self.input_cls, self.parametrs)


class WrongCoordinates(Exception):
    """This is representation of wrong coordinates."""

    def __init__(self, coordinates: list) -> None:
        """Initialization method.

        Args:
            coordinates (list): wrong coordinates.
        """
        super().__init__(coordinates)
        self.coordinates = coordinates

    def __str__(self) -> str:
        """Exception in special format."""
        return "Impossible to add or delete building on coordinates: {0}".format(self.coordinates)


class AlreadyExistingBuilding(Exception):
    """This is representation of building which already exists."""

    def __init__(self, coordinates: list) -> None:
        """Initialization method.

        Args:
            coordinates (list): wrong coordinates.
        """
        super().__init__(coordinates)
        self.coordinates = coordinates

    def __str__(self) -> str:
        """Exception in special format."""
        return "There is the building on coordinates: {0}".format(self.coordinates)


class NeverExistingBuilding(Exception):
    """This is representation of never existing building."""

    def __init__(self, coordinates: list) -> None:
        """Initialization method.

        Args:
            coordinates (list): wrong coordinates.
        """
        super().__init__(coordinates)
        self.coordinates = coordinates

    def __str__(self) -> str:
        """Exception in special format."""
        return "There isn't any building on coordinates: {0}".format(self.coordinates)


class WrongBuilding(Exception):
    """This is representation of wrong building."""

    def __str__(self) -> str:
        """Exception in special format."""
        return "You try to build something wrong not building!"


class Building:
    """The representation of building."""

    def __init__(self, height: Union[int, float], base_area: Union[int, float], number_of_floors: int) -> None:
        """Initialization method.If the building doesn't exist raises error.

        Args:
            height (Union[int, float]): building's height.
            base_area (Union[int, float]): building's base area.
            number_of_floors (int): building's number of floors.

        Raises:
            NotExisting : if the building doesn't exist.
        """
        self.height = height
        self.base_area = base_area
        self.number_of_floors = number_of_floors
        if not self.is_valid():
            raise NotExisting(__class__.__name__, [self.height, self.base_area, self.number_of_floors])

    def is_valid(self) -> bool:
        """Check the building.

        Returns:
            bool: True if it's possible to build this building else False.
        """
        conditions = []
        conditions.append(isinstance(self.height, int | float) and isinstance(self.base_area, int | float))
        conditions.append(isinstance(self.number_of_floors, int))
        if all(conditions):
            for parametr in self.__dict__.values():
                conditions.append(parametr > 0)
        return all(conditions)

    def to_dict(self) -> dict:
        """Turn building to the dict.

        Returns:
            dict: dictionary from the building.
        """
        return self.__dict__

    def __str__(self) -> str:
        """The string representation.

        Returns:
            str: how should we see the building.
        """
        return "Height: {0}\nBase area: {1}\nNumber of floors: {2}\n".format(*list(self.__dict__.values()))


class Map:
    """The representation of map."""

    def __init__(self, name: str, width: int, height: int) -> None:
        """Initialization method.If the map doesn't exist raises error.

        Args:
            name (str): map's name.
            width (int): map's width.
            height (int): map's height.

        Raises:
            NotExisting : if the map doesn't exist.
        """
        self.name = name
        self.width = width
        self.height = height
        if not self.is_valid():
            raise NotExisting(__class__.__name__, [self.name, self.width, self.height])
        self.matrix = [['0' for _ in range(self.width)] for _ in range(self.height)]
        self.list_with_buildings = []

    def __str__(self) -> str:
        """The string representation.

        Returns:
            str: how should we see the map.
        """
        necessary_len = len(self.matrix[0]) * 4 - 2 + len(self.name)
        return "\n{0}\n\n {1}".format(self.name.center(necessary_len, " "), str(np.array(self.matrix))[1:-1],)

    def is_valid(self) -> bool:
        """Check the map.

        Returns:
            bool: True if map exists else False.
        """
        conditions = []
        conditions.append(isinstance(self.name, str) and isinstance(self.width, int))
        conditions.append(isinstance(self.height, int))
        if all(conditions):
            for parametr in (self.width, self.height):
                conditions.append(parametr > 0)
        return all(conditions)

    def check_coordinate(self, x_coordinate: int, y_coordinate: int) -> bool:
        """Check coordinates.

        Args:
            x_coordinate (int): x coordinate of building.
            y_coordinate (int): y coordinate of building.

        Returns:
            bool: True if coordinates is good else False.
        """
        return isinstance(x_coordinate, int) and isinstance(y_coordinate, int)\
            and (0 <= x_coordinate < self.width) and (0 <= y_coordinate < self.height)

    def add_map_to_json(self) -> None:
        """Writes current map to json."""
        if os.path.exists("maps.json"):
            map_dictionary = {
                self.name: self.matrix,
                "width": self.width,
                "height": self.height,
                "buildings": [[]]
            }
            with open("maps.json", 'rt') as file_json:
                data_to_open = json.load(file_json)
                if map_dictionary in data_to_open["maps"]:
                    return
            with open("maps.json", 'a+') as file_json:
                file_json.seek(file_json.truncate(file_json.tell() - 2))
                file_json.write(',\n')
                data_to_write = json.dumps(map_dictionary)
                file_json.write(data_to_write)
                file_json.write(']}')
        else:
            with open("maps.json", 'wt') as file_json:
                map_dictionary = {
                    "maps": [
                        {
                            self.name: self.matrix,
                            "width": self.width,
                            "height": self.height,
                            "buildings": [[]]
                        }
                    ]
                }
                data_to_write = json.dumps(map_dictionary)
                file_json.write(data_to_write)

    def add_building(self, x_coordinate: int, y_coordinate: int, building: Building) -> None:
        """Add building to the map.

        Args:
            x_coordinate (int): x coordinate of building.
            y_coordinate (int): y coordinate of building.
            building (Building): building wich we should add on the map.

        Raises:
            WrongCoordinates: if coordinates os wrong.
            AlreadyExistingBuilding: if you try to build a building where it is.
            WrongBuilding: if you try to build something wrong not building.
        """
        if not self.check_coordinate(x_coordinate, y_coordinate):
            raise WrongCoordinates([x_coordinate, y_coordinate])
        if self.matrix[y_coordinate][x_coordinate] == 'B':
            raise AlreadyExistingBuilding([x_coordinate, y_coordinate])
        if not isinstance(building, Building):
            raise WrongBuilding
        self.matrix[y_coordinate][x_coordinate] = 'B'
        self.list_with_buildings.append((x_coordinate, y_coordinate, building))
        with open("maps.json", 'rt') as file_json:
            data_to_open = json.load(file_json)
        for maps in data_to_open["maps"]:
            if self.name in maps.keys():
                maps[self.name] = self.matrix
                maps["buildings"] += [(x_coordinate, y_coordinate, building.to_dict())]
                break
        with open("maps.json", 'wt') as file_json:
            data_to_write = json.dumps(data_to_open)
            file_json.write(data_to_write)

    def delete_building(self, x_coordinate: int, y_coordinate: int) -> None:
        """Delete building from the map.

        Args:
            x_coordinate (int): x coordinate of building.
            y_coordinate (int): y coordinate of building.

        Raises:
            WrongCoordinates: if coordinates os wrong.
            NeverExistingBuilding: if you try to delete building which isn't build.
        """
        if not self.check_coordinate(x_coordinate, y_coordinate):
            raise WrongCoordinates([x_coordinate, y_coordinate])
        if self.matrix[y_coordinate][x_coordinate] == '0':
            raise NeverExistingBuilding([x_coordinate, y_coordinate])
        self.matrix[y_coordinate][x_coordinate] = '0'
        lst = [par[0] == x_coordinate and par[1] == y_coordinate for par in self.list_with_buildings[1:]]
        ind = lst.index(True)
        del self.list_with_buildings[ind]
        with open("maps.json", 'rt') as file_json:
            data_to_open = json.load(file_json)
        lst = [list(maps.keys())[0] for maps in data_to_open["maps"]]
        ind = lst.index(self.name)
        maps = data_to_open["maps"][ind]
        maps[self.name] = self.matrix
        maps["buildings"] = self.list_with_buildings
        with open("maps.json", 'wt') as file_json:
            data_to_write = json.dumps(data_to_open)
            file_json.write(data_to_write)


class Menu:
    """The representation of menu."""

    def show_maps(self, flag_to_maps: bool, list_with_maps: List[Map]) -> None:
        """Show maps to user.

        Args:
            flag_to_maps (bool): True if maps exists else False.
            list_with_maps (List[Map]): list with maps.
        """
        if flag_to_maps:
            for maps in list_with_maps:
                print(maps)
        else:
            print("Нет доступных карт! Создайте новую!")
            return

    def add_map(self, name: str, width: str, height: str) -> None:
        """Add map to json.

        Args:
            name (str): map's name.
            width (str): map's width.
            height (str): map's height.
        """
        if width.isdigit() and height.isdigit():
            width = int(width)
            height = int(width)
        Map(name, width, height).add_map_to_json()

    def fill_list_with_maps(self) -> List[Map]:
        """Fill list with maps.

        Returns:
            List[Map]: list with maps.
        """
        list_with_maps = []
        with open("maps.json", 'rt') as file_json:
            data_to_open = json.load(file_json)
        for maps in data_to_open["maps"]:
            for names in maps.keys():
                name = names
                break
            map_to_write = Map(name, maps["width"], maps["height"])
            map_to_write.matrix = maps[name]
            map_to_write.list_with_buildings = maps["buildings"]
            list_with_maps.append(map_to_write)
        return list_with_maps

    def open_map(self, name: str, list_with_maps: List[Map], flag_to_maps: bool) -> bool:
        """Open map and show building on it.

        Args:
            name (str): map's name.
            list_with_maps (List[Map]): list with maps.
            flag_to_maps (bool): True if maps exists else False.

        Returns:
            bool: False if there isn't buildings.
        """
        if not flag_to_maps:
            print("Нет созданных карт!")
            return False
        ind = [maps.name for maps in list_with_maps].index(name)
        maps = list_with_maps[ind]
        print(maps)
        if len(maps.list_with_buildings) == 1:
            print("Зданий нет!")
            return False
        for index, list_with_params in enumerate(maps.list_with_buildings):
            if index == 0:
                continue
            print("\nBuildings:\n")
            print("X-coordinate: {0}".format(list_with_params[0]))
            print("Y-coordinate: {0}".format(list_with_params[1]))
            dct_with_building = list_with_params[2]
            bld_height = int(dct_with_building["height"])
            bld_base_area = int(dct_with_building["base_area"])
            bld_number_of_floors = int(dct_with_building["number_of_floors"])
            bld = Building(bld_height, bld_base_area, bld_number_of_floors)
            print(bld)
        return True

    def add_building(
        self, name: str, height: str, base_area: str, number_of_floors: str,\
        x_coordinate: str, y_coordinate: str, list_with_maps: List[Map]
    ):
        """Add building to the map.

        Args:
            name (str): map's name.
            height (str): builidng's height.
            base_area (str): builidng's base area.
            number_of_floors (str): builidng's number of floors.
            x_coordinate (str): builidng's x coordinate.
            y_coordinate (str): builidng's y coordinate.
            list_with_maps (List[Map]): list with maps.
        """
        list_with_params = [height, base_area, number_of_floors, x_coordinate, y_coordinate]
        if all(parametr.isdigit() for parametr in list_with_params):
            height = int(height)
            base_area = int(base_area)
            number_of_floors = int(number_of_floors)
            x_coordinate = int(x_coordinate)
            y_coordinate = int(y_coordinate)
        for maps in list_with_maps:
            if name == maps.name:
                if not maps.check_coordinate(x_coordinate, y_coordinate):
                    print(WrongCoordinates([x_coordinate, y_coordinate]))
                    return
                maps.add_building(x_coordinate, y_coordinate, Building(height, base_area, number_of_floors))
                print("Здание добавлено!")
                break
        else:
            print("Такой карты не существует! Добавить здание невозможно!")

    def delete_building(
        self, name: str, x_coordinate: str, y_coordinate: str,\
        list_with_maps: List[Map]
    ):
        """Delete building from the map.

        Args:
            name (str): map's name.
            x_coordinate (str): builidng's x coordinate.
            y_coordinate (str): builidng's y coordinate.
            list_with_maps (List[Map]): list with maps.
        """
        if x_coordinate.isdigit() and y_coordinate.isdigit():
            x_coordinate = int(x_coordinate)
            y_coordinate = int(y_coordinate)
        for maps in list_with_maps:
            if name == maps.name:
                maps.delete_building(x_coordinate, y_coordinate)
                print("Здание удалено!")
                break
        else:
            print("Такой карты не существует! Удалить здание невозможно!")

    def show_maps_names(self, list_with_maps: List[Map], flag_to_maps: bool) -> dict:
        """Show us map's names.

        Args:
            list_with_maps (List[Map]): list with maps.
            flag_to_maps (bool): True if maps exists else False.

        Returns:
            dict: map's number and map's name.
        """
        if flag_to_maps:
            return {str(number + 1): maps.name for number, maps in enumerate(list_with_maps)}
        print("Доступных карт нет!")

    def find_map_name(self, list_with_maps: List[Map], flag_to_maps: bool) -> str:
        """Find map's name with number.

        Args:
            list_with_maps (List[Map]): list with maps.
            flag_to_maps (bool): True if maps exists else False.

        Returns:
            str: map's name
        """
        maps_names = self.show_maps_names(list_with_maps, flag_to_maps)
        for num_mp, map_nam in maps_names.items():
            print("{0}: {1}".format(num_mp, map_nam))
        number = input("Введите номер карты: ")
        return maps_names[number]

    def print_second_command(self):
        """This funcrion is needed to solve too much cognitive complexity. Print second command."""
        name = input("Введите имя карты: ")
        width = input("Введите ширину карты: ")
        height = input("Введите высоту карты: ")
        try:
            self.add_map(name, width, height)
        except NotExisting as err:
            print(err)
            return
        print("Карта создана!")

    def print_third_command(self, list_with_maps: List[Map], flag_to_maps: bool):
        """This funcrion is needed to solve too much cognitive complexity. Print third command.

        Args:
            list_with_maps (List[Map]): list with maps.
            flag_to_maps (bool): True if maps exists else False.
        """
        try:
            name = self.find_map_name(list_with_maps, flag_to_maps)
        except KeyError:
            print("Такой карты не существует!")
            return
        except AttributeError:
            return
        self.open_map(name, list_with_maps, flag_to_maps)

    def print_fourth_command(self, list_with_maps: List[Map], flag_to_maps: bool):
        """This funcrion is needed to solve too much cognitive complexity. Print fourth command.

        Args:
            list_with_maps (List[Map]): list with maps.
            flag_to_maps (bool): True if maps exists else False.
        """
        try:
            name = self.find_map_name(list_with_maps, flag_to_maps)
        except KeyError:
            print("Такой карты не существует!")
            return
        except AttributeError:
            return
        self.open_map(name, list_with_maps, flag_to_maps)
        height = input("Введите высоту: ")
        base_area = input("Введите площадь основания: ")
        number_of_floors = input("Введите количество этажей: ")
        x_coordinate = input("Введите координату по х: ")
        y_coordinate = input("Введите координату по y: ")
        try:
            self.add_building(
                name, height, base_area, number_of_floors, x_coordinate,\
                y_coordinate, list_with_maps
            )
        except (WrongCoordinates, AlreadyExistingBuilding, WrongBuilding, NotExisting) as err:
            print(err)

    def print_fifth_command(self, list_with_maps: List[Map], flag_to_maps: bool):
        """This funcrion is needed to solve too much cognitive complexity. Print fifth command.

        Args:
            list_with_maps (List[Map]): list with maps.
            flag_to_maps (bool): True if maps exists else False.
        """
        try:
            name = self.find_map_name(list_with_maps, flag_to_maps)
        except KeyError:
            print("Такой карты не существует!")
            return
        except AttributeError:
            return
        if self.open_map(name, list_with_maps, flag_to_maps):
            x_coordinate = input("Введите координату по х: ")
            y_coordinate = input("Введите координату по y: ")
        else:
            return
        try:
            self.delete_building(name, x_coordinate, y_coordinate, list_with_maps)
        except (WrongCoordinates, NeverExistingBuilding) as err:
            print(err)

    def tooooo_much_complexity(self, command: str, list_with_maps: List[Map], flag_to_maps: bool) -> bool:
        """This funcrion is needed to solve too much cognitive complexity. Call all functions.

        Args:
            command (str): command which should start.
            list_with_maps (List[Map]): list with maps.
            flag_to_maps (bool): True if maps exists else False.

        Returns:
            bool: _description_
        """
        if command == "1":
            self.show_maps(flag_to_maps, list_with_maps)
        if command == "2":
            self.print_second_command()
        if command == "3":
            self.print_third_command(list_with_maps, flag_to_maps)
        if command == "4":
            self.print_fourth_command(list_with_maps, flag_to_maps)
        if command == "5":
            self.print_fifth_command(list_with_maps, flag_to_maps)
        if command == "6":
            print("Программа завершена!")
            return True
        return False

    def run(self):
        """Main running function which start's others."""
        flag_to_maps = False
        list_with_maps = []
        while True:
            if os.path.exists("maps.json"):
                flag_to_maps = True
                list_with_maps = self.fill_list_with_maps()
            print("Список команд:\n1: show_maps - показать все доступные карты\n2: add_map - добавить карту\
                \n3: open_map - открыть карту \n4: add_building - добавить здание\
                    \n5: delete_building - удалить здание\
                    \n6: quit - завершить программу")
            command = input("Введите команду: ")
            list_with_commands = ["1", "2", "3", "4", "5", "6"]
            if command not in list_with_commands:
                print("Неверная команда!")
                continue
            if self.tooooo_much_complexity(command, list_with_maps, flag_to_maps):
                break
            print("Грузится список команд!")
            sleep(2)
