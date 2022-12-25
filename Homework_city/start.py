"""This file for the terminal interface of the program."""
import ast
import logging
import os
import traceback

from pick import pick

from classes import City, House

maps = []
actions = [
    "Показать карту",
    "Добавить здание на карту",
    "Удалить здание с карты",
    "Показать параметры строения",
    "Изменить параметры строения",
    "Выйти"
]
for map_file in os.listdir(os.path.abspath("maps")):
    if map_file.endswith(".json"):
        maps.append(os.path.join(map_file))
selected, index = pick(maps, "Выберите карту:")
path_to_map = "maps/{0}".format(selected)
cur_city = City(path_to_map)
while True:
    selected, index = pick(actions, "Выберите действие:")
    if index == 0:
        print(cur_city.print_map())
        input("Нажмите любую клавишу для выхода из режима: ")
    if index == 1:
        print("Для начала необходимо создать здание")
        try:
            name = input("Введите название: ")
            height = ast.literal_eval(input("Введите высоту: "))
            base_area = ast.literal_eval(input("Введите площадь: "))
            number_of_floors = int(input("Введите количество этажей: "))
            cur_house = House(name, height, base_area, number_of_floors)
            print(cur_house)
            input("Нажмите любую клавишу для продолжения: ")
        except Exception as e:
            print("Здание не было создано в связи с ошибкой: ")
            logging.error(traceback.format_exc())
            input("Нажмите любую клавишу для выхода: ")
            continue
        try:
            print("Введите координаты")
            row = int(input("Введите строку: "))
            col = int(input("Введите столбец: "))
            cur_city.set_house(row, col, cur_house)
            print("Здание было успешно добавлено!")
            input("Нажмите любую клавишу для выхода: ")
        except Exception as e:
            print("Здание не было добавлено на карту в связи с ошибкой: ")
            logging.error(traceback.format_exc())
            input("Нажмите любую клавишу для выхода: ")

    if index == 2:
        try:
            print("Для начала введите кординаты")
            row = int(input("Введите строку: "))
            col = int(input("Введите столбец: "))
            cur_city.del_house(row, col)
            print("Здание было успешно удалено!")
            input("Нажмите любую клавишу для выхода: ")
        except Exception as e:
            print("Здание не было удалено с карты в связи с ошибкой: ")
            logging.error(traceback.format_exc())
            input("Нажмите любую клавишу для выхода: ")

    if index == 3:
        try:
            print("Для начала введите кординаты")
            row = int(input("Введите строку: "))
            col = int(input("Введите столбец: "))
            cur_house = cur_city.get_house(row, col)
            print(cur_house)
            input("Нажмите любую клавишу для выхода: ")
        except Exception as e:
            print("Здание не было показано в связи с ошибкой: ")
            logging.error(traceback.format_exc())
            input("Нажмите любую клавишу для выхода: ")

    if index == 4:
        cur_house = None
        row = None
        col = None
        try:
            print("Для начала введите кординаты")
            row = int(input("Введите строку: "))
            col = int(input("Введите столбец: "))
            cur_house = cur_city.get_house(row, col)
            print("Здание было успешно выбрано!")
            input("Нажмите любую клавишу для продолжения: ")
        except Exception as e:
            print("Здание не было выбрано в связи с ошибкой: ")
            logging.error(traceback.format_exc())
            input("Нажмите любую клавишу для выхода: ")
            continue

        try:
            selected, index_p = pick(
                ["name", "height", "base_area", "number_of_floors"], "Выберите изменяемый параметр:")
            if index_p == 0:
                new_name = input("Введите новое имя: ")
                cur_house.change_params(name=new_name)
            if index_p == 1:
                new_height = ast.literal_eval(input("Введите новую высоту: "))
                cur_house.change_params(height=new_height)
            if index_p == 2:
                new_area = ast.literal_eval(input("Введите новую площадь: "))
                cur_house.change_params(base_area=new_area)
            if index_p == 3:
                new_floors = int(input("Введите новое количество этажей: "))
                cur_house.change_params(number_of_floors=new_floors)
            cur_city.del_house(row, col)
            cur_city.set_house(row, col, cur_house)
            print("Здание было успешно изменено")
            input("Нажмите любую клавишу для выхода: ")
        except Exception as e:
            print("Здание не было изменено в связи с ошибкой: ")
            logging.error(traceback.format_exc())
            input("Нажмите любую клавишу для выхода: ")

    if index == 5:
        exit()
