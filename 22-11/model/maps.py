"""Models of maps."""

from .buildings import BasicBuilding
from .exeptions import CardError


class BasicMap:
    """Class for the BasicMap."""

    EMPTY_FIELD = " "
    BUILDING_FIELD = "B"

    def __init__(self, name: str, width: int, height: int, building_field_by_name: bool = True):
        """Creates a basic map.

        Args:
            height: int - height of the map.
            width: int - width of the map.
            name: str - name of the map.
            building_field_by_name: int - display by building's name.
        """
        self.name = name
        self.width = width
        self.height = height
        self.__buildings = {}
        self.__map = [[BasicMap.EMPTY_FIELD] * height for _ in range(width)]  # create empty game field
        self.building_field_by_name = building_field_by_name

    def check_valid_position(self, pos_x: int, pos_y: int) -> bool:
        """Checks the position for validity.

        Args:
            pos_x: int - position by x.
            pos_y: int - position by y.

        Returns:
            bool - if position is valid.
        """
        return 0 <= pos_x < self.width and 0 <= pos_y < self.height

    def add_building(self, pos_x: int, pos_y: int, build: BasicBuilding):
        """Adds building to map.

        Args:
            pos_x: int - position by x.
            pos_y: int - position by y.
            build: BasicBuilding - the map.

        Raises:
            CardError: if position not valid or position engaged.
        """
        if not self.check_valid_position(pos_x, pos_y):
            raise CardError("Position not found")

        if self.__map[pos_y][pos_x] == self.__class__.EMPTY_FIELD:
            if self.building_field_by_name:
                self.__map[pos_y][pos_x] = build.name[0]

            else:
                self.__map[pos_y][pos_x] = self.__class__.BUILDING_FIELD

            self.__buildings[(pos_x, pos_y)] = build
        else:
            raise CardError("Field with position x={0} and position y={1} not empty".format(pos_x, pos_y))

    def del_by_pos(self, pos_x, pos_y):
        """Deletes building from map by position.

        Args:
            pos_x: int - position by x.
            pos_y: int - position by y.

        Raises:
            CardError: if building not found.
        """
        if (pos_x, pos_y) in self.__buildings.keys():
            del self.__buildings[(pos_x, pos_y)]
            self.__map[pos_y][pos_x] = self.__class__.EMPTY_FIELD

        else:
            raise CardError("building not found")

    def getter_map(self):
        """Gets the map."""
        return self.__map

    def to_dict(self) -> dict:
        """Makes dict from map.

        Returns:
            dict - dictionary from the map.
        """
        builds = []
        for position, build in self.__buildings.items():
            builds.append({"position": position} | build.to_dict())
        return {"name": self.name, "width": self.width, "height": self.height,
                "building_field_by_name": self.building_field_by_name,
                "builds": builds
                }

    def get_info(self, pos_x, pos_y) -> str:
        """Gets ingo about field by position.

        Args:
            pos_x: int - position by x.
            pos_y: int - position by y.

        Raises:
            CardError: if position not found.

        Returns:
            str - info about field.
        """
        if not self.check_valid_position(pos_x, pos_y):
            raise CardError("Position not found")
        if (pos_x, pos_y) in self.__buildings.keys():
            return str(self.__buildings[(pos_x, pos_y)])

        return "Empty field"

    @staticmethod
    def check_fields(fields: list, dictionary: dict) -> bool:
        """Checks is there all fields in the dictionary.

        Args:
            fields: list - list of fields.
            dictionary: dict - dictionary with some fields.

        Returns:
            bool - true if all fields in dictionary else false.
        """
        for field in fields:
            if not (field in dictionary):
                return False
        return True

    @classmethod
    def from_dict(cls, dictionary: dict) -> object:
        """Create a BasicMap from dictionary.

        Args:
             dictionary: dict - dictionary of the new_map.

        Raises:
            CardError: if building not have some fields.

        Returns:
             BasicMap - new map.
        """
        fields = ["name", "width", "height", "builds"]
        if not BasicMap.check_fields(fields, dictionary):
            raise CardError("Building must have fields: name, height, floor, area")

        new_map = cls(dictionary["name"], dictionary["width"], dictionary["height"])
        if "building_field_by_name" in dictionary:
            new_map.building_field_by_name = dictionary["building_field_by_name"]

        for build_di in dictionary["builds"]:
            pos_x, pos_y = build_di["position"]
            build = BasicBuilding.create_build_from_dict(build_di)
            new_map.add_building(pos_x, pos_y, build)
        return new_map
