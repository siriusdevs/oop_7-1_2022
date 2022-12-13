"""Main file from which everything starts."""
import os
from map_run import map_print
from setup import START_PATH


def in_key(key, file_name):
    """Function which checks keys input.

    Args:
        key: object - object which program gets from keyboard.
        file_name: str - path to json file.
    """
    os.system('clear')
    if key == '1' and os.path.isfile(file_name):
        if input('To remove old and create new one file with such name enter y:') == 'y':
            os.remove(file_name)
    if map_print(file_name) == 'q':
        print('by')


if __name__ == '__main__':
    while True:
        os.system('clear')
        with open(START_PATH, 'r') as star:
            print(star.read())
        start = input()
        if start == '1':
            in_key(start, '{0}{1}'.format(input('Enter name: '), '.json'))
            break
        elif start == '2':
            maps = []
            for _, _, files in os.walk(os.getcwd()):
                for name in files:
                    if '.json' in name:
                        maps.append(name)
            if maps:
                print('Choose file:')
                for num, file_map in enumerate(maps):
                    print('{0}) {1}'.format(num + 1, file_map[:-5]))
                file_name = input(': ')
                try:
                    file_name = int(file_name)
                except ValueError:
                    continue
                if 0 < file_name <= len(maps) + 1:
                    in_key(start, '{0}{1}'.format(maps[file_name - 1][:-5], '.json'))
                    break
