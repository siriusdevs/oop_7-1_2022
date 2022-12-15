"""Map building and using programm."""
from json import load, dumps
from os import path
from os import system
from os import remove


class Buildings:
    """Building class with all the functions."""

    def __init__(self):
        """Initialising the building."""
        pass

    def g_valid(self, inp: list):
        """
        Function of validating the arguments of the map generating function.

        Args:
            inp(list): list of arguments
        """
        if len(inp) == 4:
            if inp[2].isdigit() and inp[3].isdigit():
                if inp[2] != '0' and inp[3] != '0':
                    return None
        return ("Invalid arguments", False)

    def o_valid(self, num: str):
        """
        Function of validating the arguments of the map importing function.

        Args:
            num(str): map's name
        """
        if not num or len(num) != 2:
            return ("Invalid arguments", False)

    def e_valid(self, inp, Map):
        """
        Function of validating the arguments of the map editing function.

        Args:
            inp(list): list of arguments
            Map(list): the Map
        """
        if not Map:
            return ("sorry, Map isn't opened", False)
        if len(inp) == 7:
            if all([x.isdigit() for x in inp[1:6]]):
                inps1 = [inp[1], inp[2], inp[5]]
                inps2 = [inp[3], inp[4]]
                y1 = all(int(x) >= 0 for x in inps1)
                y2 = all(int(x) > 0 for x in inps2)
                y3 = (int(inp[1]) + int(inp[3]) <= len(Map[0]) and int(inp[2]) + int(inp[4]) <= len(Map))
                if y1 and y2 and y3:
                    return None
        return ("Invalid arguments", False)

    def i_valid(self, inp, b_type):
        """
        Function of validating the arguments of the map info showing function.

        Args:
            inp(list): arguments
            b_type(dict): dictionary of building's types
        """
        if len(inp) == 3:
            if inp[1].isdigit() and inp[2].isdigit():
                if (int(inp[1]), int(inp[2])) in b_type.keys():
                    return None
        return ("Invalid arguments", False)

    def generate(self, x, y):
        """
        Маp generating function.

        Args:
            x(str): Map's width
            y(str): Map's height
        """
        return [[0] * int(x) for _ in range(int(y))]

    def from_file(self, name: str):
        """
        Маp importing function.

        Args:
            name(str): Map's name
        """
        name = "Builds_{0}.json".format(name)
        with open(name, 'rt') as dic:
            b_type = {}
            dic = load(dic)
            buildmap = [[0] * dic["Mapy"] for _ in range(dic["Mapx"])]
            for building in dic["Builds"]:
                b_type[(building["y"], building["x"])] = building['type']
                buildmap[building["y"]][building["x"]] = building['height']
        return buildmap, b_type

    def editing_map(self, whattodo: str, buildmap: list, b_type: dict, y_n: str = None):
        """
        Маp editing function.

        Args:
            whattodo(str): arguments
            buildmap(list): Map
            b_type(dict): Building's types
            y_n(str): confirmation
        """
        flag = 0
        coords = []
        height = int(whattodo[4])
        for y in range(int(whattodo[1]), int(whattodo[1]) + int(whattodo[3])):
            for x in range(int(whattodo[0]), int(whattodo[0]) + int(whattodo[2])):
                coords.append((x, y))
                if buildmap[y][x] > 0:
                    flag = 1
        if flag:
            if not y_n:
                if height:
                    return ("Do you want to build your buildings on top of the old ones?[y/n]", True, b_type)
                return ("Do you want to destroy these buildings?[y/n]", True, b_type)
            if y_n == 'y':
                for x1, y1 in coords:
                    buildmap[y1][x1] = height
                    b_type[(x1, y1)] = whattodo[5]
                return (buildmap, True, b_type)
            return (buildmap, False, b_type)
        for x2, y2 in coords:
            buildmap[y2][x2] = height
            b_type[(x2, y2)] = whattodo[5]
        return (buildmap, True, b_type)

    def to_file(self, buildmap: list, name: str, b_type):
        """
        Маp export function.

        Args:
            buildmap(list): Map
            name(str): Map's name
            b_type(dict): Buildings types
        """
        bulds = [(x, y) for x in range(len(buildmap[0])) for y in range(len(buildmap)) if buildmap[y][x] > 0]
        with open("Builds_{0}.json".format(name), 'wt') as fil:
            loadinf = dumps(
                {
                    'Mapx': len(buildmap),
                    'Mapy': len(buildmap[0]),
                    "Builds": [
                        {
                            "x": build[0],
                            "y": build[1],
                            "height": buildmap[build[1]][build[0]],
                            "type": b_type[(build[1], build[0])]
                        } for build in bulds
                    ]
                }
            )
            fil.write(loadinf)

    def input_analyser(self, inp: list, bmap: list, name: str, edited: bool, b_type: dict, y_n: str = None):
        """
        Function for anaysing input data.

        Args:
            inp(list): input data
            bmap(list): Map
            name(str): Map name
            edited(bool): map status
            b_type(dict): buildings types
            y_n(str): confirmation
        """
        if inp[0] == 'G':
            not_valid = self.g_valid(inp)
            if not_valid:
                return not_valid
            if path.exists('Builds_{0}.json'.format(inp[1])):
                return ("Map {0} does already exist".format(inp[1]), False)
            else:
                if bmap and edited and not y_n:
                    return ("Do you want to save your map? [y/n]", True)
                elif bmap and edited and y_n:
                    if y_n == 'y':
                        self.to_file(bmap, name)
                        bmap = self.generate(inp[2], inp[3])
                    elif y_n == 'n':
                        bmap = self.generate(inp[2], inp[3])
                else:
                    bmap = self.generate(inp[2], inp[3])
            return (bmap, inp[1], True, b_type)
        if inp[0] == 'O':
            not_valid = self.o_valid(inp)
            if not_valid:
                return not_valid
            if bmap and edited and not y_n:
                return ("Do you want to save your map? [y/n]", True)
            elif bmap and edited and y_n:
                if y_n == 'y':
                    self.to_file(bmap, name)
            try:
                return (self.from_file(inp[1])[0], inp[1], False, self.from_file(inp[1])[1])
            except Exception:
                return ("Sorry, Map {0} is damaged or doesn't exist.".format(inp[1]), False)
        if inp[0] == 'E':
            not_valid = self.e_valid(inp, bmap)
            if not_valid:
                return not_valid
            if bmap:
                bmap, edited, b_type = self.editing_map(inp[1:], bmap, b_type, y_n)
                return (bmap, name, edited, b_type)
        if inp[0] == 'S':
            self.to_file(bmap, name, b_type)
            return (bmap, name, False, b_type)
        if inp[0] == 'Q':
            if edited:
                if not y_n:
                    return ("Do you want to save it? [y/n]", True)
                else:
                    if y_n == 'y':
                        self.to_file(bmap, name, b_type)
                    elif y_n == 'n':
                        return None
        if inp[0] == 'D':
            try:
                remove("Builds_{0}.json".format(inp[1]))
            except Exception:
                return ('There is no such map here', False)
        if inp[0] == 'I':
            not_valid = self.i_valid(inp, b_type)
            if not_valid:
                return (not_valid)
            return (b_type[(int(inp[1]), (int(inp[2])))], False)

    def start(self):
        """Function that runs the programm."""
        bmap = None
        name = None
        edited = None
        itog = None
        b_type = {}
        while True:
            system('clear')
            print(("Q to quit,G to generate a map, O to open map from file, D to delete, E to edit, S to save the map,I\
 to get info about sertain building.Input structure:\nG Map's name and width by x and y separated by space\n\
O Map's name\nE building's left upper corner x and y coordinates, building's width by x and y and height of\
 the building separated by space\nD map's name\nI x and y coordinates"))
            if bmap:
                for string in bmap:
                    print(string)
            inp = input().split()
            if inp:
                itog = self.input_analyser(inp, bmap, name, edited, b_type)
            if itog:
                if isinstance(itog[0], str):
                    if itog[1]:
                        y_n = input(itog[0])
                        itog = self.input_analyser(inp, bmap, name, edited, b_type, y_n)
                        if itog:
                            bmap, name, edited, b_type = itog
                    else:
                        print(itog[0])
                        input("Enter to continue")
                else:
                    bmap, name, edited, b_type = itog
            if inp == ['Q']:
                break


if __name__ == "__main__":
    Map = Buildings()
    Map.start()
