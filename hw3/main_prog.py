"""Programm for putting buildings on the maps."""
from building_map import Building, InvalidAttribute, Map
from additional_functions.json_func import read_json, write_json
from additional_functions.directory_func import check_dir
from additional_functions.terminal_func import make_menu
from os import listdir, remove


def create_map(all_maps: list) -> str:
    """Create a map.

    Args:
        all_maps : list - list of the existing maps

    Returns:
        str - name of the file
    """
    while True:
        try:
            length = int(input('Length of your map: '))
            width = int(input('Width of your map: '))
        except ValueError:
            print('Lenght and width must be integers.')
        else:
            try:
                Map(length, width)
            except InvalidAttribute as error:
                print('InvalidAttribute: {0}'.format(error))
            else:
                break
    map_obj = Map(length, width, [[0] * width for _ in range(length)])
    file_name = 'maps/map{0}.json'.format(len(all_maps))
    write_json(file_name, map_obj.to_dict())
    print(map_obj)
    print('Map with scale: {0}x{1} was successfully saved!'.format(length, width))
    return file_name


# Choose map
def choose_map() -> str:
    """Choose a map."""
    flag = True
    while flag:
        option = make_menu(['Create map', 'Choose map', 'Quit'], 'Choose option: ')
        check_dir('maps/')
        all_maps = listdir('maps/')
        if option == 2:
            break
        elif option == 0:
            return create_map(all_maps)

        elif option == 1:
            print('Available maps:')
            if all_maps:
                flag = False
                for file_n in all_maps:
                    kwargs = read_json('maps/{0}'.format(file_n))
                    print('\n{0}\n'.format(file_n[:-5]))
                    print(Map.from_dict(**kwargs))
                options = [all_files[:-5] for all_files in all_maps]
                map_index = make_menu(options, 'Choose your map: ')
                print('\nYou have choosen {0}\n'.format(options[map_index]))
            else:
                print('No available maps.')
        if not flag:
            return 'maps/{0}'.format(all_maps[map_index])


# Put Building
def build(map_file: str) -> None:
    """Build or delete a building.

    Args:
        map_file : str - pathto the choosen map
    """
    option = make_menu(['Create building', 'Delete building', 'Quit'], 'Choose option: ')
    check_dir('buildings/')
    all_builds = listdir('buildings/')
    current_map = Map.from_dict(**read_json(map_file))
    if option == 0:
        while True:
            try:
                height = int(input("Choose height: "))
                area = int(input("Choose base area: "))
                floors = int(input("Choose number of floors: "))
            except ValueError:
                print('Height, area and floors must be integers.')
            else:
                try:
                    building = Building(height, area, floors)
                except InvalidAttribute as error:
                    print("InvalidAttribute: {0}".format(error))
                else:
                    break
        print('\n{0}\n'.format(current_map))
        while True:
            try:
                row = int(input('In which row you wanna put a building: '))
                column = int(input('In which column you wanna put a building: '))
            except ValueError:
                print('Row and column must be integers!')
            else:
                if row - 1 not in range(current_map.length) or column - 1 not in range(current_map.width):
                    print('There are no such row and column!')
                elif current_map.map_list[row - 1][column - 1] == 1:
                    print('This place is occupied! Choose another one.')
                else:
                    break
        building.location = (row, column)
        while True:
            build_name = input('Name your building: ')
            if '{0}.json' in all_builds:
                print('Such building already exists. Choose another name')
            else:
                break
        write_json('buildings/{0}.json'.format(build_name), building.to_dict())
        current_map.map_list[row - 1][column - 1] = 1
        current_map.buildings[build_name] = str(building)
        write_json(map_file, current_map.to_dict())
        print(current_map)
    elif option == 1:
        print(current_map)
        if current_map.buildings:
            options = list(current_map.buildings.keys())
            building_index = make_menu(options, 'Choose a building to delete: ')
            name_build = options[building_index]
            build_file = 'buildings/{0}.json'.format(name_build)
            build_obj = Building(**read_json(build_file))
            row, column = build_obj.location
            current_map.map_list[row - 1][column - 1] = 0
            del current_map.buildings[name_build]
            remove(build_file)
            write_json(map_file, current_map.to_dict())
            print('Building was successfully removed from the map.')
            print(current_map)
        else:
            print('There is nothing to delete.')


# Start the programm
if __name__ == '__main__':
    while True:
        curr_map = choose_map()
        if curr_map is not None:
            build(curr_map)
        option = make_menu(['Maybe one more...', 'Lets stop for now'], 'Continue building?: ')
        if option == 1:
            break
