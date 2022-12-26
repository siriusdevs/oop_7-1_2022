"""This file for class City and House."""

import json
import os
from typing import List
import exceptions


class House(object):
    """This class create a house."""

    def __init__(self, name: str, height: int or float, base_area: int or float, number_of_floors: int) -> None:
        """
        Home creation function.
        Args:
            name: str - name of house.
            height: int or float - height of house in meters.
            base_area: int or float - area of house in square meters.
            number_of_floors: int - count of floors in house.
        """
        self.par_h = [name, height, base_area, number_of_floors]

    @classmethod
    def validation_params(
            cls,
            name: str,
            height: int or float,
            base_area: int or float,
            number_of_floors: int
    ) -> bool:
        """
        The function checks the correctness of the given parameters.
        Args:
            name: str - name of house.
            height: int or float - height of house in meters.
            base_area: int or float - area of house in square meters.
            number_of_floors: int - count of floors in house.

        Returns:
            bool - if params of house is valid.

        Raises:
            InvalidHouseParams - if someone params does not int or float.
            InvalidHouseName - if name of house does not str or empty.
            NullHouseParams - if someone params is null.
        """
        bord = 0
        par_i_or_f_v = [height, base_area, number_of_floors]
        if not all(isinstance(par, (float, int)) for par in par_i_or_f_v[:2]):
            raise exceptions.InvalidHouseParams()
        if not isinstance(par_i_or_f_v[2], int):
            raise exceptions.InvalidHouseParams()
        if not isinstance(name, str) or name == "":
            raise exceptions.InvalidHouseName()
        if any(par <= bord for par in par_i_or_f_v):
            raise exceptions.NullHouseParams()
        return True

    @property
    def par_h(self):
        """
        This function return List of house params.
        Returns:
            List of current params of house.
        """
        return self._par_h

    @par_h.setter
    def par_h(self, new_params: List) -> None:
        """
        This function set new params.
        Args:
            new_params: List of new params.
        """
        value_for_size = 4
        if len(new_params) == value_for_size:
            if self.validation_params(*new_params):
                self._par_h = new_params

    def change_params(self, name=None, height=None, base_area=None, number_of_floors=None) -> None:
        """
        This function change params.
        Args:
            name: should be str if needed to be changed.
            height: should be int or float if needed to be changed.
            base_area: should be int or float if needed to be changed.
            number_of_floors: should be int if needed to be changed.

        Raises:
            NothingToChange - if nothing to change.
        """
        list_params_for_change = self._par_h
        if name or height or base_area or number_of_floors:
            if name:
                list_params_for_change[0] = name
            if height:
                list_params_for_change[1] = height
            if base_area:
                list_params_for_change[2] = base_area
            if number_of_floors:
                list_params_for_change[3] = number_of_floors
            if self.validation_params(*list_params_for_change):
                self._par_h = list_params_for_change
        else:
            raise exceptions.NothingToChange()

    def __str__(self):
        """
        This function return house params.
        Returns:
            str without params of house.
        """
        return "Params for this house:\n\
               1. name: {0}\n\
               2. height: {1}\n\
               3. base area: {2}\n\
               4. number of floors: {3}".format(*self._par_h)


class City(object):
    """This class create the city."""

    def_params = ['name', 'height', 'base_area', 'number_of_floors']

    def __init__(self, path_to_map: str) -> None:
        """
        This function create the city.
        Args:
            path_to_map: str with the path to the map.

        Raises:
            DoesntExistParamsOnMap - if params doesn't exist in map.
            MapFileDoesntExist - if file with map doesn't exist.
        """
        if os.path.exists(path_to_map) and os.path.isfile(path_to_map):
            with open(path_to_map, "rt") as map_file:
                conf_data = json.loads(map_file.read())
                try:
                    map_configuration = conf_data["map_conf"]
                    buildings = conf_data["buildings"]
                    rows = map_configuration["size_row"]
                    cols = map_configuration["size_col"]
                    count_of_houses = map_configuration["count_of_houses"]
                except KeyError:
                    raise exceptions.DoesntExistParamsOnMap()
                if self.validation_map(buildings, rows, cols, count_of_houses):
                    self.map_configuration = map_configuration
                    self.count_of_houses = count_of_houses
                    self.rows = rows
                    self.cols = cols
                    self.map = buildings
                    self.path = path_to_map
        else:
            raise exceptions.MapFileDoesntExist()

    @classmethod
    def validation_map(cls, checked_map: List, rows: int, cols: int, count_of_houses: int) -> bool:
        """
        The function is necessary to check the map for errors.
        Args:
            checked_map: list - map for checking.
            rows: int - rows of map.
            cols: int - colum of map.
            count_of_houses: int - number of houses on the map.

        Raises:
            InvalidConfigurationsMap: if any configuration map params is not int and less than or equal to 0.
            InvalidMapSize: if the length of objects on the map does not match the rows and columns.
            InvalidBuildingParams: if the parameters or their number do not correspond to the standard.
            InvalidValuesInParamsBuilding: if the parameters of the house are incorrect.
            InvalidCountOfBuildings: if count of houses doesn't correspond count of houses in configuration of map.

        Returns:
            bool - if map is valid.
        """
        conf_par = [rows, cols, count_of_houses]
        check_count_of_houses = 0
        if not all(isinstance(par, int) for par in conf_par) or any(par < 0 for par in conf_par[::2]):
            raise exceptions.InvalidConfigurationsMap()
        if len(checked_map) != rows * cols:
            raise exceptions.InvalidMapSize()
        for house in checked_map:
            if house != 'Null':
                check_count_of_houses += 1
                if list(house.keys()) != cls.def_params:
                    raise exceptions.InvalidBuildingParams()
                try:
                    House.validation_params(*house.values())
                except Exception:
                    raise exceptions.InvalidValuesInParamsBuilding()
        if not count_of_houses == check_count_of_houses:
            raise exceptions.InvalidCountOfBuildings()
        return True

    def print_map(self) -> str:
        """
        This function return str map.
        Returns:
            str: current map.
        """
        res = [[0 for _ in range(self.rows)] for _ in range(self.rows)]
        num_house = 0
        for i in range(self.rows):
            for j in range(self.rows):
                if self.map[num_house] == 'Null':
                    res[i][j] = "×"
                else:
                    res[i][j] = "⌂"
                num_house += 1
        s = "\n".join(str(i).replace(',', ' ').replace('[', '').replace(']', '').replace('\'', '') for i in res)
        return s

    def validation_rows_and_cols(self, row: int, col: int) -> bool:
        """
        This method is needed in order to check whether the given row and column values can be used.
        Args:
            row: int - selected row.
            col: int - selected column.

        Raises:
            InvalidRowOrCol: if the selected row or column cannot exist in the given map.
        """
        vals = [row, col]
        if all(par >= 0 and isinstance(par, int) for par in vals) and row < self.rows and col < self.cols:
            return True
        raise exceptions.InvalidRowOrCol()

    def get_house(self, row: int, col: int) -> House:
        """
        This method is needed to return an instance of the house from the map.
        Args:
            row: int - selected row.
            col: int - selected column.

        Returns:
            House: object of class House.

        Raises:
            NullHouseError: if house doesn't exist on this row and col.
        """
        if self.validation_rows_and_cols(row, col):
            num_house = 0
            for i in range(self.rows):
                for j in range(self.cols):
                    if i == row and j == col:
                        if self.map[num_house] != 'Null':
                            return House(*[self.map[num_house][par] for par in self.def_params])
                        else:
                            raise exceptions.NullHouseError()
                    num_house += 1

    def save_map(self) -> None:
        """
        This function is needed to save the map to a file.
        """
        self.map_configuration["count_of_houses"] = self.count_of_houses
        all_map = {"buildings": self.map, "map_conf": self.map_configuration}
        result_str = "{}".format(all_map).replace('\'', '\"')
        with open(self.path, "w") as f:
            f.write(result_str)
        f.close()

    def set_house(self, row: int, col: int, house: House) -> None:
        """
        This function is needed to put the house on the map.
        Args:
            row: int - selected row.
            col: int - selected column.
            house: object of class House.

        Raises:
            HouseInsertToHouse: if the house already exists on the map.
        """
        if self.validation_rows_and_cols(row, col):
            num_house = 0
            for i in range(self.rows):
                for j in range(self.cols):
                    if i == row and j == col:
                        if self.map[num_house] != 'Null':
                            raise exceptions.HouseInsertToHouse()
                        else:
                            self.map[num_house] = dict(zip(City.def_params, house.par_h))
                    num_house += 1
        self.count_of_houses += 1
        self.save_map()

    def del_house(self, row: int, col: int) -> None:
        """
        The function is necessary in order to remove the house from the map.
        Args:
            row: int - selected row.
            col: int - selected column.

        Raises:
            DeleteNullHouse: if house doesn't exist on map.
        """
        if self.validation_rows_and_cols(row, col):
            num_house = 0
            for i in range(self.rows):
                for j in range(self.cols):
                    if i == row and j == col:
                        if self.map[num_house] == 'Null':
                            raise exceptions.DeleteNullHouse()
                        else:
                            self.map[num_house] = 'Null'
                    num_house += 1
        self.count_of_houses -= 1
        self.save_map()
