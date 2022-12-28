"""Models of geometric buildings."""

from .exeptions import BuildingError


class BasicBuilding:
    """Class for the basic building."""

    def __init__(self, name: str, height: float, floor: int, area: float):
        """Creates a basic building.

        Args:
            height: float - height of the building.
            area: float - area of the building.
            name: str - name of the building.
            floor: int - number of floors in the building.

        Raises:
            BuildingError: if height, floor or area <=0.
            ValueError: if height, floor or area are not numeric.
        """
        if not isinstance(height, (float, int)) or not isinstance(area, (float, int)):
            raise ValueError("Height and area must be float")

        if not isinstance(floor, int):
            raise ValueError("Floor must be float")
        if height <= 0 or floor <= 0 or area <= 0:
            raise BuildingError("Area, height and floor must be above zero")
        self.__area = float(area)
        self.__height = float(height)
        self.__floor = int(floor)
        self.__name = str(name)

    def __str__(self):
        return "{0}: height - {1} floor - {2} area - {3}".format(self.__name,self.__height,self.__floor,self.__area)

    @property
    def name(self) -> str:
        """Get current value of name.

        Returns:
            float - current value of name.
        """
        return self.__name

    @name.setter
    def setter_name(self, name: str) -> None:
        """Setter for name.

        Args:
            name: str - new value for name.
        """
        self.__floor = str(name)

    @property
    def floor(self) -> int:
        """Get current value of floor.

        Returns:
            float - current value of floor.
        """
        return self.__floor

    @floor.setter
    def setter_floor(self, floor: int) -> None:
        """Setter for floor.

        Args:
            floor: int - new value for floor.

        Raises:
            ValueError : if new value not be numeric.
            BuildingError : if new value <= 0.
        """
        if isinstance(floor, int):
            self.__floor = int(floor)

        else:
            raise ValueError("Floor must be int, not {0}".format(type(floor)))
        if floor <= 0:
            raise BuildingError("floor must be above zero")

    @property
    def height(self) -> float:
        """Get current value of height.

        Returns:
            float - current value of height.
        """
        return self.__height

    @height.setter
    def setter_height(self, height: float) -> None:
        """Setter for height.

        Args:
            height: float - new value for height.

        Raises:
            ValueError : if new value not be numeric.
            BuildingError : if new value <= 0.
        """
        try:
            self.__height = float(height)
        except ValueError:
            raise ValueError("Height must be float, not {0}".format(type(height)))
        if height <= 0:
            raise BuildingError("Height must be above zero")

    @property
    def area(self) -> float:
        """Get current value of area.

        Returns:
            float - current value of area.
        """
        return self.__area

    @area.setter
    def setter_area(self, area: float) -> None:
        """Setter for area.

        Args:
            area: float - new value for area.

        Raises:
            ValueError : if new value not be numeric.
            BuildingError : if new value <= 0.
        """
        try:
            self.__area = float(area)
        except ValueError:
            raise ValueError("Area must be float, not {0}".format(type(area)))

        if area <= 0:
            raise BuildingError("Area must be above zero")

    def to_dict(self) -> dict:
        """Turns the building into a dictionary.

        Returns:
            dict - dictionary of the building.
        """
        return {"name": self.__name, "height": self.__height, "floor": self.__floor, "area": self.__area}

    @classmethod
    def create_build_from_dict(cls, dictionary: dict) -> object:
        """Create a basic building from dictionary.

        Args:
            dictionary: dict - dictionary of the building.

        Returns:
            BasicBuilding - new building.

        Raises:
            BuildingError : if dictionary doesn't have fields name, height, floor, area.
        """
        if not ("name" in dictionary and "height" in dictionary
                and "floor" in dictionary and "area" in dictionary):
            raise BuildingError("Building must have fields: name, height, floor, area")
        return cls(name=dictionary.get("name"), height=dictionary.get("height"),
                   floor=dictionary.get("floor"), area=dictionary.get("area"))
