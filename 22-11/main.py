import os

from model.buildings import BasicBuilding
from model.maps import BasicMap
import json
DEFAULT = "Default"
WORK = True
cur_map = BasicMap("", 1, 1)
# TODO переписать
COMMANDS = {1: "show map",
            2: "add building",
            3: "delete building",
            4: "show info",
            5: "switch map",
            6: "exit"
            }

def get_all_maps():
    all_files = []
    for path, dirs, files in os.walk("./maps"):
        all_files += files
    return  all_files

def display_all_maps():
    for num, map in enumerate(get_all_maps()):
        print("{0}. {1}".format(num,map))


def run():
    load_map_by_map_name(DEFAULT)
    while WORK:
        try:
            display_commands()
            command = int(input("Enter command: "))
            if command ==1 :
                show_map()
            elif command == 2:
                add_building()
            elif command == 3:
                delete_building()
            elif command == 4:
                show_info()
            elif command == 5:
                load_map()
            elif command == 6:
                exit()
        except ValueError:
            print("Invalid format")
        except IndexError:
            print("Command not found")
        except Exception as e:
            print(e)

def delete_map():
    pass

def load_map():
    global cur_map
    print("1. create new map")
    print("2. load map")
    command = int(input("Enter command: "))
    if command == 1:

        save_to_json(cur_map)
        new_map = create_map()
        cur_map = new_map
        save_to_json(cur_map)

    elif command == 2:
        display_all_maps()
        num = int(input("Enter num of map: "))
        save_to_json(cur_map)
        load_map_by_file_name(get_all_maps()[num])

def exit():
    global WORK
    save_to_json(cur_map)
    WORK = False

def save_to_json(map):
    di = map.to_dict()
    with open("maps/{0}.json".format(map.name), "w") as outfile:
        json.dump(di, outfile)

def load_map_by_map_name(name):
    global cur_map
    with open('maps/{0}.json'.format(name), 'r') as openfile:
        # Reading from json file
        cur_map = BasicMap.from_dict(json.load(openfile))


def load_map_by_file_name(name):
    global cur_map
    with open('maps/{0}'.format(name), 'r') as openfile:
        # Reading from json file
        cur_map = BasicMap.from_dict(json.load(openfile))

def display_commands():
    for num, command in COMMANDS.items():
        print("{0}. {1}".format(num,command))
def add_building():

    print("Enter information about the new building")
    pos_x = int(input("x - "))
    pos_y = int(input("y - "))
    if cur_map.check_valid_position(pos_x,pos_y):

        name = input("name - ")
        height = float(input("height - "))
        floor = int(input("floor - "))
        area = float(input("area - "))
        cur_map.add_building(pos_x,pos_y,BasicBuilding(name,height,floor,area))
    else:
        print("Position not found")


def create_map():
    print("Enter information about the new map")
    name = input("name - ")
    width = int(input("width - "))
    height = int(input("height - "))
    return  BasicMap(name,width,height)

def delete_building():
    print("Enter position of buildings")
    pos_x = int(input("x - "))
    pos_y = int(input("y - "))
    cur_map.del_by_pos(pos_x,pos_y)


def show_info():
    print("Enter position of buildings")
    pos_x = int(input("x - "))
    pos_y = int(input("y - "))
    print(cur_map.get_info(pos_x,pos_y))



def show_map():
    arr = cur_map.get_map()
    print("{}: width - {} height - {}".format(cur_map.name,cur_map.width,cur_map.height))
    for row in arr:
        print("|" + " ".join(row)+"|")
# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    maps = []
    # build= BasicBuilding("Viktor host",55.5,10,10)
    # new_map = BasicMap("lalal lend",10,10, False)
    # new_map.add_building(0,0,build)
    #
    # with open('map.json', 'r') as openfile:
    #     # Reading from json file
    #     json_object = json.load(openfile)
    # show_map(new_map.get_map())
    # get_all_maps()
    #
    # map1 = BasicMap("Default", 10, 10)
    # cur_map = map1
    # save_to_json(map1)
    run()



