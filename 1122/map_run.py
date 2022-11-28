"""File which reply for printing part of program."""


def map_print():
    """Function which prints and adds houses map.

    Returns:
        str - if program should stop running.
    """
    import os
    from street import street, House
    import time
    from functions import str_matrix, check_type, check_pos
    while True:
        time.sleep(0.5)
        os.system('clear')
        print(str_matrix())
        motion = input('motion(add/remove/q) = ')
        if motion == 'q':
            return 'q'
        if motion == 'add':
            square = input('square = ')
            height = input('height = ')
        elif motion != 'remove0':
            continue
        x_pos = input('x_pos = ')
        y_pos = input('y_pos = ')
        if check_pos(x_pos) and check_pos(y_pos) and check_type(height) and check_type(height):
            street(House(int(x_pos), int(y_pos), int(square), int(height)), motion)
