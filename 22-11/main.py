"""Main for buildings."""

import os

from model.buildings import BasicBuilding
from model.maps import BasicMap
import json


class Terminal:
    """Class for run cards in terminal."""

    CARDS_PATH = "./maps/"
    DEFAULT_CARD_NAME = "Default"

    def __init__(self, card: BasicMap = None):
        """Creates a Terminal.

        Args:
            card: BasicMap - current map model.
        """
        if card is None:
            card = BasicMap(Terminal.DEFAULT_CARD_NAME, 10, 10)
        self.card = card
        self.__COMMANDS = {1: {"name": "show map", "command": self.show_card},
                           2: {"name": "add building", "command": self.add_building},
                           3: {"name": "delete building", "command": self.delete_building},
                           4: {"name": "show info", "command": self.show_info},
                           5: {"name": "switch map", "command": self.load_card},
                           6: {"name": "delete this map", "command": self.delete_card},
                           7: {"name": "exit", "command": self.exit}
                           }
        self.__WORK = False

    def run(self):
        """Starts the terminal."""
        self.load_default()
        self.__WORK = True
        while self.__WORK:
            try:
                self.display_commands()
                command = int(input("Enter command: "))
                self.__COMMANDS[command]["command"]()
            except ValueError:
                print("Invalid format")
            except IndexError:
                print("Command not found")
            except Exception as exception:
                print(exception)

    def display_all_cards(self):
        """Displays all cards."""
        for num, card in enumerate(self.get_all_cards()):
            print("{0}. {1}".format(num, card))

    @staticmethod
    def get_all_cards():
        """Gets all list cards in default folder."""
        all_files = []
        for _, _, files in os.walk(Terminal.CARDS_PATH):
            all_files += files
        return all_files

    def delete_card(self):
        """Deletes current card."""
        os.remove(Terminal.CARDS_PATH + "{0}.json".format(self.card.name))
        print("load default map")
        self.load_default()

    def load_default(self):
        """Loads default cards."""
        if not os.path.exists(Terminal.CARDS_PATH + "{0}.json".format(Terminal.DEFAULT_CARD_NAME)):
            self.card = BasicMap(Terminal.DEFAULT_CARD_NAME, 10, 10)
            self.save_to_json()
        self.load_card_by_map_name(Terminal.DEFAULT_CARD_NAME)

    def load_card(self):
        """Loads card from list of all cards."""
        print("1. create new map")
        print("2. load map")
        command = int(input("Enter command: "))
        if command == 1:
            self.save_to_json()
            self.card = self.create_map()
            self.save_to_json()

        elif command == 2:
            self.display_all_cards()
            num = int(input("Enter num of map: "))
            self.save_to_json()
            self.load_card_by_file_name(self.get_all_cards()[num])

    def exit(self):
        """Stops the terminal."""
        self.save_to_json()
        self.__WORK = False

    def save_to_json(self):
        """Saves current card to json."""
        di = self.card.to_dict()
        if not os.path.isdir(Terminal.CARDS_PATH):
            os.mkdir(Terminal.CARDS_PATH)
        with open(Terminal.CARDS_PATH + "{0}.json".format(self.card.name), "w") as outfile:
            json.dump(di, outfile)

    def load_card_by_map_name(self, name: str):
        """Loads map by name.

        Args:
            name: str - map name.
        """
        with open('maps/{0}.json'.format(name), 'r') as openfile:
            # Reading from json file
            self.card = BasicMap.from_dict(json.load(openfile))

    def load_card_by_file_name(self, name: str):
        """Loads map by filename.

        Args:
            name: str - filename.
        """
        with open(Terminal.CARDS_PATH + "{0}".format(name), 'r') as openfile:
            # Reading from json file
            self.card = BasicMap.from_dict(json.load(openfile))

    def display_commands(self):
        """Displays all commands."""
        for num, command in self.__COMMANDS.items():
            print("{0}. {1}".format(num, command["name"]))

    def add_building(self):
        """Adds buildings to current card."""
        print("Enter information about the new building")
        pos_x = int(input("x - "))
        pos_y = int(input("y - "))
        if self.card.check_valid_position(pos_x, pos_y):

            name = input("name - ")
            height = float(input("height - "))
            floor = int(input("floor - "))
            area = float(input("area - "))
            self.card.add_building(pos_x, pos_y, BasicBuilding(name, height, floor, area))
        else:
            print("Position not found")

    @staticmethod
    def create_map():
        """Creates new map."""
        print("Enter information about the new map")
        name = input("name - ")
        width = int(input("width - "))
        height = int(input("height - "))
        return BasicMap(name, width, height)

    def delete_building(self):
        """Deletes building from current card."""
        print("Enter position of buildings")
        pos_x = int(input("x - "))
        pos_y = int(input("y - "))
        self.card.del_by_pos(pos_x, pos_y)

    def show_info(self):
        """Shows info about position on current card."""
        print("Enter position of buildings")
        pos_x = int(input("x - "))
        pos_y = int(input("y - "))
        print(self.card.get_info(pos_x, pos_y))

    def show_card(self):
        """Shows current card."""
        arr = self.card.getter_map()
        print("{0}: width - {1} height - {2}".format(self.card.name, self.card.width, self.card.height))
        print("  ", " ".join(map(str, range(0, len(arr)))))
        for num, row in enumerate(arr):
            print("{0}|".format(num), " ".join(row), "|")


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    terminal = Terminal()
    terminal.run()
