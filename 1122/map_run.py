"""File with function which prints matrix."""


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
    from functions import str_matrix, check_pos, inp_json
    while True:
        time.sleep(0.5)
        os.system('clear')
        print(' ' * (SIZE // 2) + file_name)
        print(str_matrix(file_name))
        motion = input('motion:\n1) add\n2) remove\n3) show house\n4) q\n:')
        match motion:
            case '4':
                return 'q'
            case '1':
                square = input('square = ')
                height = input('height = ')
                x_pos = input('x_pos = ')
                y_pos = input('y_pos = ')
            case '2':
                square = 1
                height = 1
                x_pos = input('x_pos = ')
                y_pos = input('y_pos = ')
            case '3':
                x_pos = input('x_pos = ')
                y_pos = input('y_pos = ')
                for cls_class in inp_json(file_name):
                    # Если честно, то мне самому не по себе из-за этих строк кода, но flake8 только так пропускает
                    if cls_class.x_pos == int(x_pos) and cls_class.y_pos == int(y_pos):
                        print(''.join(['House: {0}\nposition: ({1}, {2})\nheight: {3}\n',
                              'square: {4}'
                                       ]
                                      ).format(cls_class, cls_class.x_pos, cls_class.y_pos,
                                                     cls_class.height, cls_class.square
                                               ),
                              )
                        time.sleep(3)
                continue
            case _:
                continue
        if check_pos(x_pos) and check_pos(y_pos) and check_pos(height) and check_pos(square):
            street(House(int(x_pos), int(y_pos), int(square), int(height)), file_name, motion)
