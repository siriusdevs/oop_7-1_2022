from .buildings import BasicBuilding
from .exeptions import MapError


class BasicMap:
    EMPTY_FIELD = " "
    BUILDING_FIELD = "B"

    def __init__(self, name:str, width: int, height: int, building_field_by_name: bool = True):
        self.name = name
        self.width = width
        self.height = height
        self.__buildings = {}
        self.__map = [[BasicMap.EMPTY_FIELD] * height for _ in range(width)]  # create empty game field
        self.building_field_by_name = building_field_by_name

    def check_valid_position(self, pos_x:int, pos_y:int):
        return 0 <= pos_x < self.width or 0 <= pos_y < self.height

    def add_building(self, pos_x: int, pos_y: int, build: BasicBuilding):
        if not self.check_valid_position(pos_x,pos_y):
            raise MapError("Position not found")

        if self.__map[pos_y][pos_x] == self.__class__.EMPTY_FIELD:
            if self.building_field_by_name:
                self.__map[pos_y][pos_x] = build.name[0]

            else:
                self.__map[pos_y][pos_x] = self.__class__.BUILDING_FIELD

            self.__buildings[(pos_x, pos_y)] = build
        else:
            raise MapError("Field with position x = {0} and position y = {1} not empty".format(pos_x, pos_y))

    def del_by_pos(self, pos_x, pos_y):
        if (pos_x, pos_y) in self.__buildings.keys():
            del self.__buildings[(pos_x, pos_y)]
            self.__map[pos_y][pos_x] = self.__class__.EMPTY_FIELD

        else:
            raise MapError("building not found")

    def get_map(self):
        return self.__map

    def to_dict(self):
        builds = []
        for position, build in self.__buildings.items():
            builds.append({"position":position} | build.to_dict())
        return {"name":self.name, "width": self.width, "height":self.height ,
                "building_field_by_name" :self.building_field_by_name,
                "builds": builds
                }
    def get_info(self, pos_x, pos_y):
        if not self.check_valid_position(pos_x, pos_y):
            raise MapError("Position not found")
        if (pos_x, pos_y) in self.__buildings.keys():
            return str(self.__buildings[(pos_x, pos_y)])
        else:
            return "Empty field"

    @staticmethod
    def check_fields(fields, dictionary):
        for field in fields:
            if not field in dictionary:
                return False
        return True

    @classmethod
    def from_dict(cls, dictionary: dict) -> object:
        """Create a BasicMap from dictionary.

             Args:
                 dictionary: dict - dictionary of the new_map.

             Returns:
                 BasicMap - new new_map.
        """
        fields = ["name", "width","height","builds"]
        if not BasicMap.check_fields(fields,dictionary):
            raise MapError("Building must have fields: name, height, floor, area")

        new_map = cls(dictionary["name"], dictionary["width"], dictionary["height"])
        if "building_field_by_name" in dictionary:
            new_map.building_field_by_name = dictionary["building_field_by_name"]

        for build_di in dictionary["builds"]:
            pos_x, pos_y = build_di["position"]
            build = BasicBuilding.create_build_from_dict(build_di)
            new_map.add_building(pos_x, pos_y, build)
        return new_map
