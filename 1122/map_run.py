"""File with function which prints matrix."""


message = 'House: {0}\nposition: ({1}, {2})\nheight: {3}\nsquare: {4}'


def show_house(file_name, position):
    """Function which shows parameters of house.

    Args:
        file_name: str - name of file with json.
        position: tuple - coordinates x and y.
    """
    from functions import inp_json
    import time
    for cls_class in inp_json(file_name):
        if cls_class.x_pos == int(position[0]) and cls_class.y_pos == int(position[1]):
            args = [cls_class, cls_class.x_pos, cls_class.y_pos, cls_class.height, cls_class.square]
            print(args)
            print(''.join(message).format(*args))
            time.sleep(3)


def map_print(file_name):
    """Function which prints and adds houses map.

    Args:
        file_name: str - path to json file.

    Returns:
        str - if program should stop running.
    """
    import os
    from street import street, House
    import time
    from setup import SIZE
    from functions import str_matrix, check
    while True:
        time.sleep(0.5)
        os.system('clear')
        print(' ' * (SIZE // 2) + file_name)
        print(str_matrix(file_name))
        action = input('action:\n1) add\n2) remove\n3) show house\n4) q\n:')
        position = (input('x_pos = '), input('y_pos = '))
        match action:
            case '4':
                return 'q'
            case '1':
                size = (input('square = '), input('height = '))
            case '2':
                size = (1, 1)
            case '3':
                show_house(file_name, position)
                continue
            case _:
                continue
        if check(position[0], 0, SIZE - 1) and check(position[1], 0, SIZE - 1) and check(size[1]) and check(size[0]):
            street(House(int(position[0]), int(position[1]), int(size[1]), int(size[0])), file_name, action)
