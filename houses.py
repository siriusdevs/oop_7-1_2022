import json
import os
from pick import pick
import time

class Building:
    def __init__(self, height, base_area, floors) -> None:
        if int(height) <= 0 or int(base_area) <= 0 or int(floors) <= 0:
            raise ValueError
        self.height = height
        self.base_area = base_area
        self.floors = floors

all_maps = []
workflow = {}


def write_json(new_data):
    global name_of_file
    with open(name_of_file,'r+') as file:
        file_data = json.load(file)
        file_data["houses"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
     

def choose_action():
    global name_of_file, map_list
    name, index = pick(["Создать дом", "Удалить дом"], "Выберите действие:")
    if index == 0:
        build()
    if index == 1:
        delete()
    

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
        time.sleep(2)
        delete()
    for i in range(len(dict["houses"])):
        if str(row) + str(column) ==  list(dict["houses"][i].keys())[0]:
            dict["houses"].pop(i)
            with open(name_of_file, "w") as file:
                json.dump(dict, file)
            choose()


def build():
    global name_of_file, map_list
    title = 'Выберите колонку с домом: '
    option, row = pick(map_list, title)
    title = 'Выберите дом: '
    option, column = pick(map_list[int(row)], title)
    if map_list[row][column] == 1:
        print("Тут уже есть дом, выберите другую клетку")
        time.sleep(2)
        build()
    height = input("Введите высоту дома: ")
    base_area = input("Введите площадь основания дома: ")
    floors = input("Введите количество этажей дома: ")
    b = Building(height, base_area, floors)
    res = {}
    res[str(row) + str(column)] = b.__dict__
    write_json(res)
    choose()
        

def new_map():
    global map_list, name_of_file
    name_of_file = input("Введите новое имя для карты без расширения\n") + ".json"
    if name_of_file not in all_maps:
        workflow = {}
        size = int(input("Введите размерность карты: "))
        map_list = [[0] * size for _ in range(size)]
        workflow = {"houses": [], "size": size}
        with open(name_of_file, "w") as file:
            json.dump(workflow, file)
        build()
    else:
        print("Это имя занято :(")
        new_map()


def existing_map():
    global all_maps, name_of_file, map_list
    name_of_file, row = pick(all_maps, "Выберите карту")
    if name_of_file in all_maps:
        with open(name_of_file, 'r') as j:
            workflow.update(json.loads(j.read()))
        size = workflow["size"]
        map_list = [[0] * size for _ in range(size)]
        cells = []
        for i in range(len(workflow["houses"])):
            cells.append(list(workflow["houses"][i].keys())[0])
        for i in cells:
            map_list[int(i[0])][int(i[1])] = 1
        choose_action()
    else:
        print("Такой файл не найден")


def choose():
    global all_maps
    all_maps = []
    for file in os.listdir(os.path.dirname(os.path.abspath(__file__))):
        if file.endswith(".json"):
            all_maps.append(os.path.join(file))
    re = input("Хотите создать новую карту, использовать имеющиеся, или выйти? Введите 1, 2 или 3 для выбора\n")
    if re == "1":
        new_map()
    elif re == "2":
        existing_map()
    elif re == "3":
        print()
    else:
        print("Некорректный ввод")
        choose()

name_of_file = ""
map_list = []

if __name__ == "__main__":
    for file in os.listdir(os.path.dirname(os.path.abspath(__file__))):
        if file.endswith(".json"):
            all_maps.append(os.path.join(file))
    print("У вас имеется {} файла(ов) карт".format(len(all_maps)))
    print(str(all_maps))
    choose()
