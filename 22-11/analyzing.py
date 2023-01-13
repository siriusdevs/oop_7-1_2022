"""Function for anaysing and transmitting input data."""

from os import path, remove, listdir
from functions import Functions


class Buildings(Functions):
    """Building class with all the functions."""

    def __init__(self, inp: list = None, bmap: tuple = None, edited: bool = False, y_n: str = None):
        """
        Function for initialiing class.

        Args:
            inp(list): input data
            bmap(tuple): Map with buildings and name
            edited(bool): map status
            y_n(str): confirmation
        """
        self.inp = inp
        self.bmap = bmap
        self.edited = edited
        self.y_n = y_n

    def to_generate(self):
        """Generate the map please."""
        not_valid = self.g_valid(self.inp)
        if not_valid:
            return not_valid
        if path.exists('Builds_{0}.json'.format(self.inp[1])):
            return ("Map {0} does already exist".format(self.inp[1]), False)
        if self.bmap and self.edited and not self.y_n:
            return ("Do you want to save your map? [y/n]", True)
        if self.bmap and self.edited and self.y_n:
            if self.y_n == 'y':
                self.to_file(self.bmap, self.name, self.builds_type)
        self.bmap = self.generate(self.inp[2], self.inp[3])
        return (self.bmap, self.inp[1], True, self.builds_type)

    def to_open(self):
        """Open the map please."""
        not_valid = self.o_valid(self.inp)
        if not_valid:
            return not_valid
        if self.bmap and self.edited and not self.y_n:
            return ("Do you want to save your map? [y/n]", True)
        elif self.bmap and self.edited and self.y_n:
            if self.y_n == 'y':
                self.to_file(self.bmap, self.name, self.builds_type)
        try:
            return (self.from_file(self.inp[1])[0], self.inp[1], False, self.from_file(self.inp[1])[1])
        except Exception:
            return ("Sorry, Map {0} is damaged or doesn't exist.".format(self.inp[1]), False)

    def to_edit(self):
        """Edit the map, please."""
        not_valid = self.e_valid(self.inp, self.bmap)
        if not_valid:
            return not_valid
        if self.bmap:
            self.bmap, self.edited, self.builds_type = \
                self.editing_map(self.inp[1:], self.bmap, self.builds_type, self.y_n)
            return (self.bmap, self.name, self.edited, self.builds_type)

    def to_quit(self):
        """Quit, please."""
        if self.edited:
            if not self.y_n:
                return ("Do you want to save it? [y/n]", True)
            if self.y_n == 'y':
                self.to_file(self.bmap, self.name, self.builds_type)
            elif self.y_n == 'n':
                return None

    def to_delete(self):
        """Delete this map, please."""
        try:
            remove("Builds_{0}.json".format(self.inp[1]))
        except Exception:
            return ('There is no such map here', False)

    def to_show_info(self):
        """Show the Info, please."""
        not_valid = self.i_valid(self.inp, self.builds_type)
        if not_valid:
            return (not_valid)
        return (self.builds_type[(int(self.inp[1]), (int(self.inp[2])))], False)

    def to_show_list(self):
        """Show the list of available maps."""
        print("\nAvailabe maps:")
        for build in listdir():
            if build[:7] + build[-5:] == 'Builds_.json':
                print(build[7:-5])
        return ("", False)

    def input_analys(self):
        """Function for anaysing input data."""
        self.bmap, self.builds_type, self.name = self.bmap
        if self.inp[0] == 'G':
            return self.to_generate()
        if self.inp[0] == 'O':
            return self.to_open()
        if self.inp[0] == 'E':
            return self.to_edit()
        if self.inp[0] == 'S':
            self.to_file(self.bmap, self.name, self.builds_type)
            return (self.bmap, self.name, False, self.builds_type)
        if self.inp[0] == 'Q':
            return self.to_quit()
        if self.inp[0] == 'D':
            return self.to_delete()
        if self.inp[0] == 'I':
            return self.to_show_info()
        if self.inp[0] == 'L':
            return self.to_show_list()
