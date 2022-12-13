"""Terminal menu."""


def make_menu(options: list, ask: str) -> int:
    """Make a terminal menu.

    Args:
        options : list - options in the menu
        ask : str - ask to choose option
    """
    count_opt = len(options)
    for index, option in enumerate(options):
        print('{0} -- {1}'.format(index, option))
    while True:
        try:
            option_index = int(input(ask))
        except ValueError:
            print('Invalid option. Please enter a number between 0 and {0}'.format(count_opt - 1))
        else:
            if option_index not in range(count_opt):
                print('Invalid option. Please enter a number between 0 and {0}'.format(count_opt - 1))
            else:
                break
    return option_index
