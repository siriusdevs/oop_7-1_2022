from map import *
from faker import Faker 
from random import randint

class Menu:

    @staticmethod
    def start():
        #os.system('clear')

        def mapper_city(sel_city):
            def select_house(sel):
                def txt_house(houses):
                    text = ""
                    for house in houses:
                        text += " ".join(house) + "\n"
                    return text
                keyboard = list(map(lambda x: list(map(str, x)), map_city.cities[sel].selecter()))
                x, y = 0, 0
                flag = keyboard[y][x]
                keyboard[y][x] = "\33[7m" + keyboard[y][x] + "\33[0m"
                while True:
                    os.system("clear")
                    sel_city = input("\n\33[34msel - Выбрать дом\
                                \ngb - Вернуться назад\33[0m\
                                \n\n{}\
                                \n\33[33m     w - вверх\
                                \na - влево, d -вправо\
                                \n     s - вниз{:^216}\
                                \n\nВведите команду: ".format(txt_house(keyboard), "\33[34mq - выйти\33[0m"))
                    if sel_city in ["gb", "sel", "q"]:
                        break
                    elif sel_city in ["a", "d"]:
                        if sel_city == "a":
                            keyboard[y][x] = flag 
                            x -= 1
                            if x < 0:
                                x = len(keyboard[0])-1
                            flag = keyboard[y][x]
                            keyboard[y][x] = "\33[7m" + keyboard[y][x] + "\33[0m"
                        if sel_city == "d":
                            keyboard[y][x] = flag 
                            x += 1
                            if x > len(keyboard[0])-1:
                                x = 0
                            flag = keyboard[y][x]
                            keyboard[y][x] = "\33[7m" + keyboard[y][x] + "\33[0m"
                    elif sel_city in ["w", "s"]:
                        if sel_city == "w":
                            keyboard[y][x] = flag 
                            y -= 1
                            if y < 0:
                                y = len(keyboard)-1
                            flag = keyboard[y][x]
                            keyboard[y][x] = "\33[7m" + keyboard[y][x] + "\33[0m"
                        if sel_city == "s":
                            keyboard[y][x] = flag 
                            y += 1
                            if y > len(keyboard)-1:
                                y = 0
                            flag = keyboard[y][x]
                            keyboard[y][x] = "\33[7m" + keyboard[y][x] + "\33[0m"
                    else:
                        print("Введите корректную команду")
                if sel_city == "sel":
                    house = None
                    for _ in map_city.cities[sel].houses:
                        for __ in _:
                            if __.coordinate == list(map(str, [x, y])):
                                house = __
                    return house
                elif sel_city == "q":
                    return "q"
                elif sel_city == "gb":
                    mapper()

            def mapper_house(sel_city):
                def option_house(house):
                    if not house.count_floors:
                        os.system("clear")
                        while 1:
                            sel_option = input("{}\
                                \n\33[34m1. Создать дом\
                                \n2. Снести дом\
                                \n3. Вернуться обратно{:^216}\
                                \n\nВведите номер команды: ".format(house, "q - выйти\33[0m"))
                            if sel_option in ["1", "2", "3", "q"]:
                                    break
                    else:
                        while 1:
                            os.system("clear")
                            sel_option = input("{}\
                                \n\33[34m1. Перестроить дом\
                                \n2. Снести дом\
                                \n3. Вернуться обратно{:^216}\
                                \n\nВведите номер команды: ".format(house, "q - выйти\33[0m"))
                            if sel_option in ["1", "2", "3", "q"]:
                                break
                    return sel_option
                house = select_house(sel_city)
                if house == "q":
                    raise SystemExit                 
                sel = option_house(house)
                if sel == "1":
                    if house.change_option():
                        map_city.cities[sel_city].save_city()
                    else:
                        raise SystemExit
                    mapper_house(sel_city)
                elif sel == "2":
                    house.delete_house()
                    map_city.cities[sel_city].save_city()
                    mapper_house(sel_city)
                elif sel == "3":
                    mapper_house(sel_city)
            mapper_house(sel_city)

        def del_city(num):
            cities = Map.get_cities().cities
            key = list(cities.keys())
            cities.pop(key[num])
            with open('{}map.json'.format(Config().PWD), 'w') as file:
                file.write(dumps(cities))

        def mapper():
            map_pj = map_city.selecter()
            num = 0
            while True:
                os.system("clear")
                sel_city = input("\33[34mnew - Создать новый город?\
                                \ndel - Удалить город\
                                \nsel - Выбрать город\33[0m\
                              \n\n{}\
                               \n\33[33ma - влево, d - вправо{:^216}\
                              \n\nВведите команду: ".format(map_pj[num], "\33[34mq - выйти\33[0m"))
                if sel_city in ["del", "new", "sel", "q"]:
                    break
                elif sel_city in ["a", "d"]:
                    if sel_city == "a":
                        num -= 1
                        if num < 0:
                            num = len(map_pj)-1
                    if sel_city == "d":
                        num += 1
                        if num > len(map_pj)-1:
                            num = 0
                else:
                    print("Введите корректную команду")
            if sel_city == "sel":
                mapper_city(num)
                pass
            elif sel_city == "del":
                del_city(num)
                Menu.start()
            elif sel_city == "q":
                pass
            else:
                Menu.create_city()
                mapper()



        map_city = Map.get_cities()
        if map_city != 0:
            mapper()
            pass
        else:
            Menu.create_city(False)

    @staticmethod
    def create_city(n_sing_city=True):
        os.system('clear')
        if n_sing_city:
            while 1:
                sel = int(input("1. Да\
                               \n2. Нет\
                             \n\nВведите номер: "))
                if sel == 1 or sel == 2:
                    break
                else:
                    print("Введите номер цифрой!")
            if sel == 1:
                name = input("Введите название города: ")
                if name == "random":
                    name = Faker().name().split()[0] + "burg"
                length = input("Введите длину проекции города: ")
                if length == "random":
                    length = randint(0, 20)
                weigth = input("Введите ширину проекции города: ")
                if weigth == "random":
                    weigth = randint(0, 20)
                City(name, [length, weigth]).new_city()
                Menu.start()
        else:
            name = input("Введите название города: ")
            if name == "random":
                name = Faker().name().split()[0] + "burg"
            length = input("Введите длину проекции города: ")
            if length == "random":
                length = randint(0, 20)
            weigth = input("Введите ширину проекции города: ")
            if weigth == "random":
                weigth = randint(0, 20)
            City(name, [length, weigth]).new_city()
            Menu.start()

Menu.start()