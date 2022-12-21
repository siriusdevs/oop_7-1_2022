"""File with functions for other files."""


def check(num, left_bound=0, right_bound=None):
    """Function checks number for valid.

    Args:
        num: str - position x or y.
        left_bound: int - numbers could not be lower left_bound.
        right_bound: int - numbers could not be larger right_bound.

    Returns:
        bool - if num is valid.
    """
    try:
        num = int(num)
    except ValueError:
        return False
    if right_bound:
        return left_bound <= num <= right_bound
    return left_bound < num


def inp_json(file_name):
    """Function reads json file.

    Args:
        file_name: str - path to json file.

    Returns:
        list - list of classes House.
        list - empty list if there is no json file.
    """
    import json
    import os
    from street import House
    if os.path.isfile(file_name):
        with open(file_name, 'rt') as map_list:
            street_map = json.load(map_list)
            ans = []
            for line in street_map.values():
                arr = list(str(line).replace(',', '').replace('(', '').replace(')', '').replace("'", "").split())
                ans.append([int(lst) for lst in arr[:-1] if check(lst, 0)] + [arr[-1]])
            return [House(*lst) for lst in ans]
    return []


def lst_matrix(file_name):
    """Function which fills matrix.

    Args:
        file_name: str - path to json file.

    Returns:
        matrix: list - list of numbers 0 and 1.
    """
    from setup import SIZE
    matrix = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    array_of_classes = inp_json(file_name)
    for cls_class in array_of_classes:
        matrix[cls_class.y_pos][cls_class.x_pos] = 1
    return matrix


def str_matrix(file_name):
    """Function turns matrix to string.

    Args:
        file_name: str - path to json file.

    Returns:
       str - matrix in string type.
    """
    matrix = lst_matrix(file_name)
    res = ''
    for line in matrix:
        res = '{0}{1}\n'.format(res, line)
    return res
