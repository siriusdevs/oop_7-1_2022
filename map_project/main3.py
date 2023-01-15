"""The Map and Building program"""

import json


class Building:
    """Building class to store information about a building"""

    def __init__(self, height, area, floors):
        """
        Initializes a Building object with given height, area and floors

        Args:
             height: int, height of the building
             area: int, area of the building
             floors: int, number of floors in the building
        """
        self.height = height
        self.area = area
        self.floors = floors


class Map:
    """Map class to store information about a map and its buildings"""

    def __init__(self, size):
        """
        Initializes a Map object with given size

        Args:
            size: int, size of the map
        """
        self.size = size
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
        Removes a building object from the map

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
                b = Building(building["height"], building["area"], building["floors"])
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
        data = []
        for building in buildings:
            b = {"height": building.height, "area": building.area, "floors": building.floors}
            data.append(b)
        json.dump(data, f)


def main():
    """Entry point of the program."""
    map_size = None
    try:
        with open("map.json", "r") as f:
            data = json.load(f)
            map_size = data["size"]
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        map_size = input("Enter map size: ")
        with open("map.json", "w") as f:
            json.dump({"size": map_size}, f)

    buildings = load_data()
    map = Map(map_size)
    for building in buildings:
        map.add_building(building)

    while True:
        print("1. Add building")
        print("2. Remove building")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            height = int(input("Enter building height: "))
            area = int(input("Enter building area: "))
            floors = int(input("Enter number of floors: "))
            if height == 0 or area == 0 or floors == 0:
                print("Height, area, and floors must be greater than 0.")
                continue
            building = Building(height, area, floors)
            map.add_building(building)
            buildings.append(building)
            save_data(buildings)
        elif choice == "2":
            for i, building in enumerate(buildings):
                print(f"{i+1}. {building.height}, {building.area}, {building.floors}")
            choice = int(input("Enter the number of the building you want to remove: "))
            building = buildings[choice - 1]
            map.remove_building(building)
            buildings.remove(building)
            save_data(buildings)
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
