import os
from typing import List
from pick import pick
import json
from time import sleep

all_maps = []
workflow = {}

class Map_worker:
    def map_checker():
        for file in os.listdir():
            if file.endswith(".json") and not file in all_maps:
                all_maps.append(os.path.join(file))
        return input("Было найдено карт с домами: {}\nДоступны данные карты: {}\nНажмите Enter клавишу для продолжения "\
                    .format(len(set(all_maps)), set(all_maps)))

    def choose(self):
        global all_maps
        os.system('cls||clear')
        Map_worker.map_checker()
        os.system('cls||clear')
        while True:
            selected, index = pick(['Создать новую карту', 'Редактировать текущую'\
                                    , 'Выйти из программы', 'Посмотреть карту'], 'Набор функций:')
            if index == 0:
                Map_worker.create_map()
            elif index == 1:
                Map_worker.map_selection()
            elif index == 2:
                os.system('cls||clear')
                exit()
            elif index == 3:
                Map_worker.show_map()

    def create_map():
        global map_list, name_of_file
        name_of_file = input("Введите имя для карты без расширения\n") + ".json"
        if name_of_file not in all_maps:
            workflow = {}
            width = int(input("Введите ширину карты: "))
            height = int(input("Введите высоту карты: "))
            map_list = [[0] * width for _ in range(height)]
            workflow = {"houses": [], "height": height, "width": width}
            with open(name_of_file, "w") as file:
                json.dump(workflow, file)
            Building.build()
        else:
            print("Это имя занято :(")
            Map_worker.create_map()

    def read_map():
        global name_of_file
        if name_of_file in all_maps:
            with open(name_of_file, "rt") as map_file:
                conf_data = json.loads(map_file.read())
        map_configuration = conf_data["map_conf"]
        buildings = conf_data["buildings"]
        rows = map_configuration["size_row"]
    
    
    def show_map():
        global all_maps, name_of_file, map_list
        name_of_file, row = pick(all_maps, "Выберите карту")
        if name_of_file in all_maps:
            with open(name_of_file, 'r') as j:
                workflow.update(json.loads(j.read()))
            width = workflow["width"]
            height = workflow["height"]
            map_list = [[0] * width for _ in range(height)]
            cells = []
            for i in range(len(workflow["houses"])):
                cells.append(list(workflow["houses"][i].keys())[0])
            for i in cells:
                map_list[int(i[0])][int(i[1])] = 1
        print('Ваша карта собсна: \n')
        for row in map_list:
            print(row)
        sleep(3)
        Map_worker.choose('')


    def map_selection():
        global all_maps, name_of_file, map_list
        name_of_file, row = pick(all_maps, "Выберите карту")
        if name_of_file in all_maps:
            with open(name_of_file, 'r') as j:
                workflow.update(json.loads(j.read()))
            width = workflow["width"]
            height = workflow["height"]
            map_list = [[0] * width for _ in range(height)]
            cells = []
            for i in range(len(workflow["houses"])):
                cells.append(list(workflow["houses"][i].keys())[0])
            for i in cells:
                map_list[int(i[0])][int(i[1])] = 1
            Map_worker.action()
        else:
            print("Такой файл не найден")

    def action():
        global name_of_file, map_list
        name, index = pick(["Создать дом", "Удалить дом", 'Выйти из программы'], "Выберите действие:")
        if index == 0:
            Building.build()
        if index == 1:
            Building.delete()
       


class Building:
    def __init__(self, height: int, area: int, floor: int):
        self.height = height
        self.area = area
        self.floor = floor



    def write_json(new_data):
        global name_of_file
        with open(name_of_file,'r+') as file:
            file_data = json.load(file)
            file_data["houses"].append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent = 4)

    def build(*args):
        selected, row_1 = pick(map_list, 'Выберите область для редактирования: ')
        selected, row_2 = pick(map_list[row_1], 'Выберите дом: ')
        if map_list[row_1][row_2] == 1:
            input("Тут уже есть дом, выберите другую клетку")
            Building.build()
        height = input("Введите высоту дома: ")
        area = input("Введите площадь основания дома: ")
        floor = input("Введите количество этажей дома: ")
        temp = Building(height, area, floor)
        temp_data = {}
        temp_data[str(row_1) + str(row_2)] = temp.__dict__
        Building.write_json(temp_data)
        Map_worker.choose('')

    def delete():
        global name_of_file, map_list
        print(name_of_file)
        with open(name_of_file, encoding="utf8") as file:
            dict = json.load(file)
        title = 'Выберите колонку с домом: '
        option, row = pick(map_list, title)
        title = 'Выберите дом: '
        option, column = pick(map_list[int(row)], title)
        if map_list[row][column] == 0:
            print("Тут ничего нет, выберите другую клетку")
            Building.delete()
        for i in range(len(dict["houses"])):
            if str(row) + str(column) ==  list(dict["houses"][i].keys())[0]:
                dict["houses"].pop(i)
                with open(name_of_file, "w") as file:
                    json.dump(dict, file)
                Map_worker.choose('')

a = Map_worker()
print(a.choose())