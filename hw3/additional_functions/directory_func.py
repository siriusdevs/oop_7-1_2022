"""Check directory."""
from os import path, getcwd, mkdir


def check_dir(directory: str) -> None:
    """Check whether a directory exists or not. If not, creates one in a current working directory.

    Args:
        directory : str - directory that must be checked
    """
    if not path.isdir(directory):
        mkdir('{0}/{1}'.format(getcwd(), directory))
