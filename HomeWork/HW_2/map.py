from math import floor
from time import sleep
import os
from typing import List
from json import dumps, load


class ImpossibleHouse(Exception):
    """This error means that a house with such parameters cannot be built."""

    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> None:
        """Exception in special format."""
        return "These options caused an error ImpossibleHouse"

class ImpossibleCity(Exception):
    """This error means that a City with such parameters cannot be built."""

    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> None:
        """Exception in special format."""
        return "These options caused an error ImpossibleCity"

class ImpossibleStructureMap(Exception):
    """This error arose due to the incorrect structure of map.json."""

    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> None:
        """Exception in special format."""
        return "map.json struct was causing error ImpossibleStructureMap"

class House:
    """This is a representation of the house\Это изображение дома."""

    def __init__(self, height: float, base_area: float, count_floors: int, coordinate=[0, 0], name=None) -> None:
        """This method takes the parameters of the house and remembers them\
        Метод получает параметры и запоминает их.

        Arguments:
            height(float): Height of the represented house\Высота изображаемого дома.
            base_area(float): Base area of the represented house\Площадь основания изображаемого дома.
            count_floors(int): Number of floors of the presented house\Количество этажей изображаемого дома.
        Raises:
            NonexistentFigure: if the figure cannot exist.
        """
        self.height = height
        self.base_area = base_area
        self.count_floors = count_floors
        self.if_valid()
        self.coordinate = coordinate
        if name:
            self.name = name
        elif all([self.height, self.base_area, self.count_floors]):
            self.name = "Неизвестная постройка"
        else:
            self.name = "Площадка для стройки"

    def to_dict(self):
        """This method allows you to work with the class as a dictionary,
        where the key name is the name of the variable,
        and the value is the value of the variable\
        Данный метод позволяет работать с классом как с словарём,
        где ключ - это имя переменой,
        а значение словаря - значение переменной.
        """
        return self.__dict__

    def __str__(self):
        """This magic method creates a string representation of the class representation of the class\
        Данный магический метод создаёт строковое представление класса.    
        """
        if self.height and self.base_area and self.count_floors:
            return '''\33[33m{0}\
                \33[31m\nВысота дома: {1}\
                \nПлощадь основания дома: {2}\
                \nКоличество этажей: {3}\
                \n{4}я улица {5}й дом\n\33[0m'''.format(self.name,\
                                                  self.height,\
                                                  self.base_area,\
                                                  self.count_floors,\
                                                  int(self.coordinate[1]) + 1,\
                                                  int(self.coordinate[0]) + 1)
        else:
            return "\33[32mЗдесь ещё нет дома(((\n\33[0m"

    def change_option(self):
        """This method is to make changes to the home view settings\
        Этот метод внесения изменений в параметры изображаемого дома(Строительства и перестройки дома).
        """
        if self.height and self.base_area and self.count_floors:
            while 1:
                os.system("clear")
                sel = input("\33[32mЧто хотите изменить?\n\33[0m\
                            \n1. Высота постройки\
                            \n2. Площадь оcнования постройки\
                            \n3. Наименование постройки\
                            \n4. Вернуться обратно{:^216}\
                            \n\nВведите номер команды: ".format("q - выйти"))
                if sel == "1":
                    self.height = float(input("Введите высоту постройки: "))
                    self.count_floors = floor(self.height / 2.5)
                    self.if_valid()
                    print("\u001bc")
                    break
                elif sel == "2":
                    self.base_area = float(input("Введите площадь основания постройки: "))
                    self.if_valid()
                    print("\u001bc")
                    break
                elif sel == "3":
                    self.name = input("Введите название постройки: ")
                    print("\u001bc")
                    break
                elif sel == "4":
                    break
                elif sel == "q":
                    return False
        else:
            os.system("clear")
            self.name = input("Введите название постройки: ")
            self.height = float(input("Введите высоту постройки: "))
            self.count_floors = floor(self.height / 2.5)
            self.base_area = float(input("Введите площадь основания постройки: "))
            self.if_valid()
            print("\u001bc")
        return True

    def delete_house(self):
        """This method is designed to reset all parameters (demolition) of the house\
        Этот метод предназначен для обнуления всех параметров (сноса) дома.
        """
        self.height = None
        self.base_area = None
        self.count_floors = None
        self.name = "Площадка для стройки"

    def if_valid(self):
        val_type = (int, float)
        if all([self.height, self.base_area, self.count_floors]):
            if all([isinstance(x, val_type) for x in [self.height, self.base_area, self.count_floors]]):
                if all([x > 0 for x in [self.height, self.base_area, self.count_floors]]): 
                    self.height = float(self.height)
                    self.base_area = float(self.base_area)
                    self.count_floors = floor(self.height / 2.5)
                    return True
                else:
                    raise ImpossibleHouse
                    
            else:
                raise ImpossibleHouse


class City:
    """This is a representation of the City\Это изображение города."""

    def __init__(self, name: str, size: List[int], houses=None, sort=False) -> None:
        """This method takes the parameters of the city and remembers them\
        Метод получает параметры и запоминает их.

        Arguments:
            name(str): Name of the represented city\Название изображаемого города.
            size(List(int)): Number of streets and houses of the represented city\Количество улиц и домов изображаемого дома.
        """
        self.name = name
        self.length = size[0]
        self.weigth = size[1]
        self.if_valid()
        self.houses = houses
        self.sort = sort

    def new_city(self, PWD=None, title_map="map"):
        """This function writes a new city to a file, recreates it if the file does not exist\
        Эта функция записывает новый город в файл, исоздаёт его если файла нет."""
        if Map.get_cities() == 0:
            cities = ""
        elif os.path.exists('{}{}.json'.format(Config(PWD, title_map).PWD, Config(PWD, title_map).title_map)):
            cities = Map.get_cities().cities
        else:
            cities = ""
        with open('{}{}.json'.format(Config(PWD, title_map).PWD, Config(PWD, title_map).title_map), 'w') as file:
            houses = [[self.length, self.weigth]]
            for y in range(self.length):
                for x in range(self.weigth):
                    houses.append({"{0} {1}".format(x, y): House(None, None, None).to_dict()})
            data = {"{0}".format(self.name): houses}
            if cities != "":
                data = {**cities, **data}
            file.write(dumps(data))

    def save_city(self, PWD=None, title_map="map"):
        """This method saves all changes to the map\
        Этот метод сохраняет все изменения в карте.
        """
        if os.path.exists('{}{}.json'.format(Config(PWD, title_map).PWD, Config(PWD, title_map).title_map)):
            cities = Map.get_cities().cities
        else:
            cities = ""
        city_dict = {"{}".format(self.name): [[self.length, self.weigth]]}
        for street in self.houses:
            for house in street:
                city_dict["{}".format(self.name)].append({"{0} {1}".format(house.coordinate[0], house.coordinate[1]):
                                                         {"name": house.name,
                                                          "height": house.height,
                                                          "base_area": house.base_area,
                                                          "count_floors": house.count_floors,
                                                          "coordinate": list(map(int, house.coordinate))}})
        with open('{}{}.json'.format(Config(PWD, title_map).PWD, Config(PWD, title_map).title_map), 'w') as file:
            if cities != "":
                data = {**cities, **city_dict}
            file.write(dumps(data))

    def sort_city(self):
        """This method puts all the houses in their places on the map\
        Этот метод ставит все дома на свои места на карте.
        """
        houses = [[None for _ in range(self.weigth)] for __ in range(self.length)]
        for house in self.houses:
            coordinate = list(map(int, house.coordinate))
            houses[coordinate[1]][coordinate[0]] = house
        self.houses = houses
        self.sort = True

    def projection_city(self):
        """This method returns a projection of the city's houses where 1 house exists and 0 house does not exist\
        Этот метод возвращает проекцию домов города, где 1 дом существует и 0 дом не существует.
        """
        if self.sort:
            houses = []
            for street in self.houses:
                street_house = []
                for house in street:
                    if house.height and house.base_area and house.count_floors:
                        street_house.append(1)
                    else:
                        street_house.append(0)
                houses.append(street_house)
            return houses

    def __str__(self):
        """This magic method creates a string representation of the class representation of the class\
        Данный магический метод создаёт строковое представление класса.    
        """
        text = ""
        if self.sort:
            for street in self.projection_city():
                text += "\t" + str(street) + "\n"
        else:
            self.sort_city()
            for street in self.projection_city():
                text += "\t" + str(street) + "\n"
        return text

    def selecter(self):
        """This method returns the projection of the city, if the city is not sorted sort it\
        Этот метод возвращает проекцию города, если город не отсортирован сортирует его.
        """
        if self.sort:
            city = self.projection_city()
        else:
            self.sort_city()
            city = self.projection_city()
            self.save_city()
        return city

    def if_valid(self):
        val_type = (int, float)
        if all([self.length, self.weigth]):
            if all([isinstance(x, val_type) for x in [self.length, self.weigth]]):
                if all([x > 0 for x in [self.length, self.weigth]]): 
                    self.length = int(self.length)
                    self.weigth = int(self.weigth)
                    return True
                else:
                    raise ImpossibleCity
            else:
                raise ImpossibleCity
        else:
            raise ImpossibleCity

class Map:
    """This map\Это карта."""

    def __init__(self, cities=dict, structure=False):
        """This method takes the parameters of the city and remembers them\
        Метод получает параметры и запоминает их.

        Arguments:
            ciies(dict): A dictionary consisting of cities in which there are houses with empty or not valid parameters\
                Словарь состоящий из городов в которых есть дома с пустыми или не путыми параметрамию.
            structur(bool): If the argument is false, then the dictionary consists of other dictionaries,\
                if the argument is true, the dictionary consists of classes\
                Если аргумент ложный значит словарь состоит из других словарей,\
                если аргумент правда словарь состоит из классов.
        """
        self.cities = cities
        self.structure = structure
        self.if_valid()

    @classmethod
    def get_cities(cls, PWD=None, title_map="map"):
        """This class method reads js and returns a dictionary\
        Этот метод класса читает js и возвращает словарь.
        """
        if os.path.exists('{}{}.json'.format(Config(PWD, title_map).PWD, Config(PWD, title_map).title_map)):
            with open('{}{}.json'.format(Config(PWD, title_map).PWD, Config(PWD, title_map).title_map), 'r+', encoding='utf-8') as file:
                cities = load(file)
                return cls(cities)
        return 0

    def generate_cities(self):
        """Replaces a dictionary from dictionaries with a dictionary from classes\
        Replaces a dictionary from dictionaries with a dictionary from classes.
        """
        if not self.structure:
            cities = []
            for city in self.cities.items():
                houses = []
                sizes = city[1][0]
                name = city[0]
                city = city[1][1:]
                for house in city:
                    house = list(house.items())[0]
                    coordinate = house[0].split()
                    houses.append(House(house[1]['height'],\
                                        house[1]['base_area'],\
                                        house[1]['count_floors'],\
                                        [coordinate[0], coordinate[1]]))
                cities.append(City(name, sizes, houses))
            self.cities = cities

    def sort_cites(self):
        """This method structures the class\
        Этот метод структурирует класс.
        """
        if not self.structure:
            for city in self.cities:
                city.sort_city()
                self.structure = True

    def projection_map(self):
        """This method returns a projection of cities\
        Этот метод возвращает проекцию городов."""
        self.generate_cities()
        self.sort_cites()
        cities_name = {}
        cities = self.cities
        projection_cities = {}
        print(self.cities)
        for city in self.cities:
            print(type(city))
            cities_name[city.name] = city.projection_city()
        for city in cities_name.keys():
            count = 0
            for street_house in cities_name[city]:
                count += sum(street_house)
            projection_cities[city] = count
        return [projection_cities, cities]

    def __str__(self):
        """This magic method creates a string representation of the class representation of the class\
        Данный магический метод создаёт строковое представление класса.    
        """
        return self.selecter()

    def selecter(self):
        """This method returns a map projection.\
        Этот метод возвращает проекцию карты."""
        if self.cities != 0:
            projection = self.projection_map()
            projection_cities = projection[0]
            cities = projection[1]
            city_map = []
            for map, city in zip(projection_cities.keys(), cities):
                city_map.append("Город {0}:\n\tКоличество домов - {1}\n{2}".format(map,
                                projection_cities[map], city))
            return city_map

    def if_valid(self):
        val_type = (dict, City)
        if not self.structure:
            if all([isinstance(self.cities[x], list) for x in list(self.cities.keys())]):
                helpe = [[all([isinstance(__, dict) for __ in x[1:]]), isinstance(x[0], list)] for x in [self.cities[_] for _ in list(self.cities.keys())]]
                if all(helpe):
                    pass
                else:
                    raise ImpossibleStructureMap
            else:
                raise ImpossibleStructureMap 
        elif self.structure:
            if all([isinstance(self.cities[x], City) for x in self.cities]):
                pass
            else:
                raise ImpossibleStructureMap


class Config:
    """This configuration\Это параметры файла"""

    def __init__(self, PWD=None, title_map="map"):
        """A method that receives and remembers the file configuration"""
        import os
        from inspect import getsourcefile 
        if PWD:
            self.PWD = PWD
        else:
            pwf = os.path.abspath(getsourcefile(lambda:0))
            self.PWD = pwf.replace(os.path.basename(pwf), "")
        self.title_map = title_map


