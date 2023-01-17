"""All the functions for analyzing one."""
from json import load, dumps


class Functions:
    """Class that has functions."""

    @staticmethod
    def g_valid(inp: list):
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

    @staticmethod
    def o_valid(num: str):
        """
        Function of validating the arguments of the map importing function.

        Args:
            num(str): map's name
        """
        if not num or len(num) != 2:
            return ("Invalid arguments", False)

    @staticmethod
    def e_valid(inp, bmap):
        """
        Function of validating the arguments of the map editing function.

        Args:
            inp(list): list of arguments
            bmap(list): the map of buildings
        """
        if not bmap:
            return ("sorry, Map isn't opened", False)
        if len(inp) == 7:
            if all([x.isdigit() for x in inp[1:6]]):
                inps1 = [inp[1], inp[2], inp[5]]
                inps2 = [inp[3], inp[4]]
                y1 = all(int(x) >= 0 for x in inps1)
                y2 = all(int(x) > 0 for x in inps2)
                y3 = (int(inp[1]) < len(bmap[0]) and int(inp[2]) < len(bmap))
                if y1 and y2 and y3:
                    return None
        return ("Invalid arguments", False)

    @staticmethod
    def i_valid(inp, b_type):
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
                return ("Nothing", False)
        return ("Invalid arguments", False)

    @staticmethod
    def generate(x, y):
        """
        Маp generating function.

        Args:
            x(str): Map's width
            y(str): Map's height
        """
        return [[0] * int(x) for _ in range(int(y))]

    @staticmethod
    def from_file(name: str):
        """
        Маp importing function.

        Args:
            name(str): Map's name

        Raises:
            ValueError: если есть не то здание
        """
        name = "Builds_{0}.json".format(name)
        with open(name, 'rt') as dic:
            b_type = {}
            dic = load(dic)
            buildmap = [[0] * dic["Mapy"] for _ in range(dic["Mapx"])]
            for building in dic["Builds"]:
                if building['height'] <= 0:
                    raise ValueError
                b_type[(building["x"], building["y"])] = building['type']
                buildmap[building["y"]][building["x"]] = building['height']
        return buildmap, b_type

    @staticmethod
    def editing_map(whattodo: str, buildmap: list, b_type: dict, y_n: str = None):
        """
        Маp editing function.

        Args:
            whattodo(str): arguments
            buildmap(list): Map
            b_type(dict): Building's types
            y_n(str): confirmation
        """
        x = int(whattodo[0])
        y = int(whattodo[1])
        if buildmap[y][x]:
            if not y_n:
                if int(whattodo[4]):
                    return ("Do you want to build your building on top of the old one?[y/n]", True, b_type)
                return ("Do you want to destroy this building?[y/n]", True, b_type)
            if y_n != 'y':
                return (buildmap, False, b_type)
        buildmap[y][x] = int(whattodo[4])
        b_type[(x, y)] = (
            "{0}. {1} by x and {2} by y, {3} floors hight.".format(
                whattodo[5],
                whattodo[2],
                whattodo[3],
                whattodo[4]
                )
            )
        return (buildmap, True, b_type)

    @staticmethod
    def to_file(buildmap: list, name: str, b_type):
        """
        Маp exporting function.

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
                            "type": b_type[(build[0], build[1])]
                        } for build in bulds
                    ]
                }
            )
            fil.write(loadinf)
