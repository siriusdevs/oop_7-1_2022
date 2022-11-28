"""Main file from which everything starts."""
import os
from map_run import map_print
from setup import START_PATH, JSON_PATH


def in_key(key):
    """Function which checks keys input.

    Args:
        key: object - object which program gets from keyboard.
    """
    os.system('clear')
    if key == 'start' and os.path.isfile(JSON_PATH):
        os.remove(JSON_PATH)
    if map_print() == 'q':
        print('by')


if __name__ == '__main__':
    while True:
        os.system('clear')
        with open(START_PATH, 'r') as star:
            print(star.read())
        start = input()
        if start in {'start', 'load'}:
            in_key(start)
            break
