"""Make a terminal menu."""
from simple_term_menu import TerminalMenu


def make_menu(options: list, title: str) -> int:
    """Make a terminal menu.

    Args:
        options : list - options in the menu
        title : str - title of the menu
    """
    terminal_menu = TerminalMenu(options, title=title)
    return terminal_menu.show()
