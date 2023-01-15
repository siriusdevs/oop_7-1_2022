"""Homes classes."""


import json
import os


class InvalidKey(Exception):
    """InvalidKey error of houses."""

    def __str__(self):
        """Magic method of error."""
        return 'Unknown key found'


class DictNotFound(Exception):
    """DictNotFound error of houses."""

    def __str__(self):
        """Magic method of error."""
        return 'The dictionary not found'


class SymmetryError(Exception):
    """SymmetryError error of houses."""

    def __str__(self):
        """Magic method of error."""
        return "The map isn't symmetrical"


class HomeNotExist(Exception):
    """HomeNotExist error of houses."""

    def __str__(self):
        """Magic method of error."""
        return 'There is no such house'


class IncorrectData(Exception):
    """IncorrectData error of houses."""

    def __str__(self):
        """Magic method of error."""
        return 'Incorrect data entered'


class NotExistingConf(Exception):
    """If config isn't exsiting."""

    def __str__(self):
        """Magic method of error."""
        return 'Incorrect config'


class Homes():
    """Class of homes config."""

    def __init__(self, config='homes.json'):
        """Initialization of homes.

        Args:
            config (str): config with houses.

        Raises:
            NotExistingConf: if conf of homes isn't existing.
        """
        self.config = config
        if self.check_existing():
            self.load_data()
            self.map()
        else:
            raise NotExistingConf

    def check_existing(self):
        """This method checks if exist map."""
        for _, _, files in os.walk('./maps/'):
            data_check = files
        return self.config in data_check

    def load_data(self):
        """This method loads data from the config.

        Raises:
            KeyError: if found unknown key.
            ValueError: if conf not exists.
        """
        with open('./maps/{0}'.format(self.config), 'rt') as cur_conf:
            cur_data = cur_conf.read()
            try:
                conf_data = json.loads(cur_data)
            except Exception:
                print('An error has occurred: {0}'.format(Exception))
                raise ValueError
            try:
                self.char = conf_data['homes']
            except KeyError:
                print('An error has occurred: {0}'.format(KeyError))
                raise KeyError
            self.max_x, self.max_y = 0, 0
            for itemik in self.char:
                self.max_x = max(self.max_x, itemik['position'][0])
                self.max_y = max(self.max_y, itemik['position'][1])
            self.check_config()

    def check_config(self):
        """This method checks the validity of the data.

        Raises:
            InvalidKey: if found unknown key.
            ValueError: if type of data isn't correct.
            DictNotFound: if not found the dictionary.
        """
        keys = {'height', 'floors', 'square', 'position', 'not_exist'}
        check1 = {jtemd for itemh in self.char for jtemd in itemh} & keys
        if not check1:
            raise InvalidKey
        check2 = all([isinstance(arr, (int, float, list)) for itemf in self.char for arr in itemf.values()])
        if not check2:
            raise ValueError
        check3 = all([isinstance(itemk, dict) for itemk in self.char])
        if not check3:
            raise DictNotFound
        # check4 = self.max_x * self.max_y == len(self.char)
        # if not check4:
        #     raise SymmetryError

    def new_data(self):
        """This method write new data in config."""
        with open('./maps/{0}'.format(self.config), 'wt') as cur_file:
            nw_data = json.dumps({'homes': self.char})
            cur_file.write(nw_data)

    def map(self):
        """This method draws map of houses."""
        self.matrix = [[0 for _ in range(self.max_y)] for _ in range(self.max_x)]
        for itemgh in self.char:
            if itemgh['not_exist'] == 0:
                x_pos, y_pos = itemgh['position'][0] - 1, itemgh['position'][1] - 1
                self.matrix[x_pos][y_pos] = 1

    def __str__(self):
        """Magic method, he returns map of houses."""
        return ''.join(['{0}\n'.format(homz) for homz in self.matrix])

    def check_data_add(self, choice1, choice2):
        """This method checks data.

        Args:
            choice1 (int): first coordinate of house.S
            choice2 (int): second coordinate of house.

        Returns:
            _bool_: result of work.
        """
        choices = [choice1, choice2]
        if not all([isinstance(itemz, int) for itemz in choices]):
            return False
        if not all(itemj > 0 for itemj in choices):
            return False
        if self.max_x < choice1 or self.max_y < choice2:
            return False
        for jtem in self.char:
            if jtem['position'] == choices and jtem['not_exist'] == 1:
                return True
        return False

    def add_home(self, choice1, choice2, height, square, floors):
        """This method can create house.

        Args:
            choice1 (int): the first coordinate.
            choice2 (int): the second coordinate.
            height (float): the height of house.
            square (float): the square of house.
            floors (float): the number of floors.

        Raises:
            IncorrectData: if data isn't correct.

        Returns:
            _str_: result of work.
        """
        charks = [height, square, floors]
        if not all([isinstance(itemv, (int, float)) for itemv in charks]):
            raise IncorrectData
        if not all(itemp > 0 for itemp in charks):
            raise IncorrectData
        if self.check_data_add(choice1, choice2):
            for jtem in self.char:
                if jtem['position'] == [choice1, choice2] and jtem['not_exist'] == 1:
                    jtem['not_exist'] = 0
                    jtem['height'] = height
                    jtem['floors'] = square
                    jtem['square'] = floors
                    self.new_data()
                    return True
        return False

    def new_map(self, size1, size2, map_name):
        """This method creates new map.

        Args:
            size1 (int): number of cols.
            size2 (int): numbers of rows.
            map_name (str): name of map.

        Raises:
            IncorrectData: if data isn't correct.

        Returns:
            _bool_: result of work.
        """
        sizes = (size1, size2)
        if not all(itemjk > 0 for itemjk in sizes):
            raise IncorrectData
        if not all([isinstance(itemkj, int) for itemkj in sizes]):
            raise IncorrectData
        new_config = []
        for arr11 in range(1, size1 + 1):
            for arr22 in range(1, size2 + 1):
                harki = {"not_exist": 1, "position": [arr11, arr22]}
                new_config.append(harki)
        with open('./maps/{0}'.format(map_name), 'wt') as cur_fle:
            cur_dt = json.dumps({'homes': new_config})
            cur_fle.write(cur_dt)
            return True

    def delete_home(self, choice1, choice2):
        """This method deletes a house.

        Args:
            choice1 (int): the first coordinate.
            choice2 (int): the second coordinate.

        Raises:
            IncorrectData: if data isn't correct.

        Returns:
            _str_: result of work.
        """
        choices = [choice1, choice2]
        if not all(iteml > 0 for iteml in choices):
            raise IncorrectData
        if not all([isinstance(itemlz, int) for itemlz in choices]):
            raise IncorrectData
        for jtem in self.char:
            if jtem['position'] == choices and jtem['not_exist'] == 0:
                jtem['not_exist'] = 1
                del jtem['height']
                del jtem['floors']
                del jtem['square']
                self.new_data()
                return True
        return False

    def inform(self, choice1, choice2):
        """Returns info about house.

        Args:
            choice1 (int): the first coordinate.
            choice2 (int): the second coordinate.

        Raises:
            IncorrectData: if data isn't correct.

        Returns:
            _str_: result of work.
        """
        choices = [choice1, choice2]
        if not all(itempl > 0 for itempl in choices):
            raise IncorrectData
        if not all([isinstance(itemkn, int) for itemkn in choices]):
            raise IncorrectData
        for jtem in self.char:
            if jtem['position'] == choices and jtem['not_exist'] == 0:
                return 'Height: {0}, square: {1}, floors: {2}'.\
                    format(jtem['height'], jtem['square'], jtem['floors'])
        return False


class Menu():
    """Class menu of class Homes."""

    ERROR = 'The parameter must be greater than zero'
    INCORRECT_DATA = "Incorrect data entered"
    INCORRECT_COORDINATES = 'Incorrect coordinates of the house'

    @staticmethod
    def main(flag_menu=True):
        """Main method of menu.

        Args:
            flag_menu (bool, optional): flag for map selection. Defaults to True.
        """
        while True:
            if flag_menu:
                map_inp = input('1 - create new map\n2 - default map\
                    \n3 - select existing map\nSelect optinion: ')
                if map_inp == '2':
                    selected_map = 'homes.json'
                    flag_menu = False

                elif map_inp == '3':
                    for _, _, files in os.walk('./maps'):
                        map_houses = files
                    for ivalue in enumerate(map_houses):
                        print('{0} - {1}'.format(ivalue[0] + 1, map_houses[ivalue[0]]))
                    try:
                        inp_ds = int(input('Select number of map: '))
                    except Exception:
                        print(Menu.INCORRECT_DATA)
                        continue
                    if 1 <= inp_ds <= len(map_houses):
                        selected_map = map_houses[inp_ds - 1]
                        flag_menu = False
                    else:
                        print('Try again!')

                elif map_inp == '1':
                    try:
                        try_map = input('Enter name of map: ')
                    except Exception:
                        print(Menu.INCORRECT_DATA)
                        continue
                    name_of_map = ''.join([try_map, '.json'])
                    try:
                        size_rows = int(input('Select a number of rows: '))
                    except Exception:
                        print(Menu.INCORRECT_DATA)
                        continue
                    try:
                        cnt_of_houses = int(input('Select a number of houses in row: '))
                    except Exception:
                        print(Menu.INCORRECT_DATA)
                        continue
                    inp_data = [size_rows, cnt_of_houses]
                    if all(dt > 0 for dt in inp_data):
                        Homes().new_map(size_rows, cnt_of_houses, name_of_map)
                        selected_map = name_of_map
                        flag_menu = False
                    else:
                        print(Menu.ERROR)
                else:
                    print('Try again!')
            else:

                print(Homes(selected_map))
                print('List of commands:\n1 - add home\n2 - delete home\
                    \n3 - info about home\n4 - select map\n5 - exit')
                command = input('Select a command: ')

                if command == '1':
                    try:
                        choice1 = int(input('Select a row: '))
                    except Exception:
                        print(Menu.INCORRECT_DATA)
                        continue
                    try:
                        choice2 = int(input('Select a house: '))
                    except Exception:
                        print(Menu.INCORRECT_DATA)
                        continue
                    if not Homes(selected_map).check_data_add(choice1, choice2):
                        print(Menu.INCORRECT_COORDINATES)
                        continue
                    try:
                        height = float(input('Enter the height: '))
                    except Exception:
                        print(Menu.INCORRECT_DATA)
                        continue
                    try:
                        square = float(input('Enter the square: '))
                    except Exception:
                        print(Menu.INCORRECT_DATA)
                        continue
                    try:
                        floors = float(input('Enter the number of floors: '))
                    except Exception:
                        print(Menu.INCORRECT_DATA)
                        continue
                    par = [choice1, choice2, height, square, floors]
                    if all(cur_par > 0 for cur_par in par):
                        print(Homes(selected_map).add_home(choice1, choice2, height, square, floors))
                        print('The house is created!')
                    else:
                        print(Menu.ERROR)
                elif command in {'2', '3'}:
                    try:
                        choice1 = int(input('Select a row: '))
                    except Exception:
                        print(Menu.INCORRECT_DATA)
                        continue
                    try:
                        choice2 = int(input('Select a house: '))
                    except Exception:
                        print(Menu.INCORRECT_DATA)
                        continue
                    par = [choice1, choice2]
                    if all(coordinate > 0 for coordinate in par):
                        if command == '2' and Homes(selected_map).delete_home(choice1, choice2):
                            # Homes(selected_map).delete_home(choice1, choice2)
                            print('The house has been removed!')
                        elif command == '3' and Homes(selected_map).inform(choice1, choice2):
                            print(Homes(selected_map).inform(choice1, choice2))
                        else:
                            print(Menu.INCORRECT_COORDINATES)
                    else:
                        print(Menu.ERROR)

                elif command == '4':
                    flag_menu = True
                    continue

                elif command == '5':
                    print('Good-bye!')
                    break

                else:
                    print("Try again!")
