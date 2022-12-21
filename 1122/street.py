"""File with class House and writing information into json file functions."""
import time


class House:
    """Class creates houses."""

    def __init__(self, x_pos: int = 0, y_pos: int = 0, square: int = 1, height: int = 1, name: str = 'new_obj'):
        """Function initialises parameters of houses and checks them.

        Args:
            x_pos: int - x coordinate.
            y_pos: int - y coordinate.
            square: int - first parameter of house.
            height: int - second parameter of house.
            name: str - name of house.

        Raises:
            ValueError: Exception - error if function check False.
        """
        self.square = square
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.name = name
        if not self.check():
            raise ValueError

    def check(self) -> bool:
        """Function which checks parameters.

        Returns:
            bool - if type of parameters is int or float and no index error returns True.
        """
        from setup import SIZE
        valid = {self.square: (float, int), self.height: (float, int), self.x_pos: int, self.y_pos: int}
        if all([self.square, self.height]) > 0 and 0 <= self.x_pos <= SIZE and 0 <= self.y_pos <= SIZE:
            return all(isinstance(attr, lst_val) for attr, lst_val in valid.items())
        return False


def for_remove(file_name: str, new_house: str):
    """Function for checking position of house for remove.

    Args:
        file_name: str - name of map.
        new_house: str - house object.
    """
    from functions import inp_json, lst_matrix

    houses = inp_json(file_name)
    map_matrix = lst_matrix(file_name)
    map_matrix[new_house.y_pos][new_house.x_pos] = 0
    for cls_class in houses:
        if cls_class.x_pos == new_house.x_pos and cls_class.y_pos == new_house.y_pos:
            houses.remove(cls_class)
            return houses
        else:
            print('Там нет здания')
            time.sleep(3)


def street(new_house: House, file_name: str, action: str = '1'):
    """Function which controls file and matrix actions.

    Args:
        new_house: House - class which function must add/remove.
        action: str - what function must do.
        file_name: str - path to json file.
    """
    import json
    from functions import inp_json, lst_matrix

    houses = inp_json(file_name)
    map_matrix = lst_matrix(file_name)
    if action == '1' and map_matrix[new_house.y_pos][new_house.x_pos] == 0:
        map_matrix[new_house.y_pos][new_house.x_pos] = 1
        houses.append(new_house)
    elif action == '1' and map_matrix[new_house.y_pos][new_house.x_pos] == 1:
        print('Там уже есть здание')
        time.sleep(3)
    if action == '2':
        new_houses = for_remove(file_name, new_house)
        houses = new_houses if new_houses else []

    with open(file_name, 'w') as map_list:
        class_obj = {str(ind): str((ind.x_pos, ind.y_pos, ind.square, ind.height, ind.name)) for ind in houses}
        map_list.write(json.dumps(class_obj))


if __name__ == '__main__':
    # You can make 3 motions
    street()
