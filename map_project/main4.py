"""The Map and Building program"""

import json


class Building:
    """Building class to store information about a building"""

    def __init__(self, height, area, floors, x, y):
        """
        Initializes a Building object with given height, area and floors.

        Args:
            height (int): height of the building
            area (int): area of the building
            floors (int): number of floors in the building
            x (int): x coordinate of the building location
            y (int): y coordinate of the building location
        """
        self.height = height
        self.area = area
        self.floors = floors
        self.x = x
        self.y = y


class Map:
    """Map class to store information about a map and its buildings"""

    def __init__(self, x_size, y_size):
        """
        Initializes a Map object with given size

        Args:
            x_size (int): x size of the map
            y_size (int): y size of the map
        """
        self.x_size = x_size
        self.y_size = y_size
        self.buildings = []

    def add_building(self, building):
        """
        Adds a building object to the map

        Args:
            building: Building, the building object to be added
        """
        self.buildings.append(building)

    def remove_building(self, building):
        """
        Removes a building object from the map.

        Args:
            building: Building, the building object to be removed
        """
        self.buildings.remove(building)


def load_data():
    """
    Loads building data from a json file

    Returns:
         list, list of building objects
    """
    try:
        with open("buildings.json", "r") as f:
            data = json.load(f)
            buildings = []
            for building in data:
                b = Building(building["height"], building["area"], building["floors"], building["x"], building["y"])
                buildings.append(b)
            return buildings
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []


def save_data(buildings):
    """
    Saves building data to a json file

    Args:
        buildings: list, list of building objects
    """
    with open("buildings.json", "w") as f:
        with open("buildings.json", "w") as f:
            data = []
            for building in buildings:
                b = {"height": building.height, "area": building.area, "floors": building.floors, "x": building.x,
                     "y": building.y}
                data.append(b)
            json.dump(data, f)


def main():
    """Entry point of the program."""
    map_x_size = None
    map_y_size = None
    try:
        with open("map.json", "r") as f:
            data = json.load(f)
            map_x_size = data["x_size"]
            map_y_size = data["y_size"]
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        map_x_size = int(input("Enter map x size: "))
        map_y_size = int(input("Enter map y size: "))
        with open("map.json", "w") as f:
            json.dump({"x_size": map_x_size, "y_size": map_y_size}, f)

    buildings = load_data()
    map = Map(map_x_size, map_y_size)
    for building in buildings:
        map.add_building(building)

    while True:
        print("1. Add building")
        print("2. Remove building")
        print("3. Check buildings")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            height = int(input("Enter building height: "))
            area = int(input("Enter building area: "))
            floors = int(input("Enter number of floors: "))
            x = int(input("Enter the x coordinate of the building location: "))
            y = int(input("Enter the y coordinate of the building location: "))
            if x > map.x_size or y > map.y_size:
                print("Coordinate is outside of the map size.")
                continue
            if height <= 0 or area <= 0 or floors <= 0 or x <= 0 or y <= 0:
                print("Height, area, floors or coordinates must be greater than 0.")
                continue
            occupied = False
            for building in buildings:
                if building.x == x and building.y == y:
                    occupied = True
                    break
            if occupied:
                print("This location is already occupied.")
                continue
            building = Building(height, area, floors, x, y)
            map.add_building(building)
            buildings.append(building)
            save_data(buildings)
            print(f"{height}, {area}, {floors}, {x}, {y}")
        elif choice == "2":
            for i, building in enumerate(buildings):
                print(f"{i+1}. {building.height}, {building.area}, {building.floors}, {building.x}, {building.y}")
            choice = int(input("Enter the number of the building you want to remove: "))
            building = buildings[choice - 1]
            map.remove_building(building)
            buildings.remove(building)
            save_data(buildings)
        elif choice == "3":
            for i, building in enumerate(buildings):
                print(f"{i+1}. {building.height}, {building.area}, {building.floors}, {building.x}, {building.y}")
        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
