"""File with functions for other files."""


def check_pos(num):
    """Function checks number for valid.

    Args:
        num: str - position x or y.

    Returns:
        bool - if num is valid.
    """
    from setup import SIZE
    try:
        num = int(num)
    except ValueError:
        return False
    return 0 <= num <= SIZE - 1


def check_type(num):
    """Function checks type of num.

    Args:
        num: str - height or square.

    Returns:
        bool - True if num is int and > 0.
    """
    try:
        num = int(num)
    except ValueError:
        return False
    return num > 0


def inp_json():
    """Function reads json file.

    Returns:
        list - list of classes House.
        list - empty list if there is no json file.
    """
    import json
    import os
    from setup import JSON_PATH
    from street import House
    if os.path.isfile(JSON_PATH):
        with open(JSON_PATH, 'rt') as map_list:
            street_map = json.load(map_list)
            ans = []
            for line in street_map.values():
                arr = list(line.replace(',', '').replace('(', '').replace(')', '').split())
                ans.append([int(lst) for lst in arr])
            return [House(*lst) for lst in ans]
    return []


def lst_matrix():
    """Function which fills matrix.

    Returns:
        matrix: list - list of numbers 0 and 1.
    """
    from setup import SIZE
    matrix = [[0] * SIZE for _ in range(SIZE)]
    array_of_classes = inp_json()
    for cls_class in array_of_classes:
        matrix[cls_class.y_pos][cls_class.x_pos] = 1
    return matrix


def str_matrix():
    """Function turns matrix to string."""
    matrix = lst_matrix()
    res = ''
    for line in matrix:
        res = '{0}{1}\n'.format(res, line)
    return res
