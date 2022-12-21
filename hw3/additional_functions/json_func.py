"""Functions for work with json files."""
import json


def read_json(file_name: str) -> dict:
    """Read json file.

    Args:
        file_name : str - name of the file that must be opened
    """
    with open(file_name, 'rt') as opened_file:
        return json.load(opened_file)


def write_json(file_name: str, given_data: dict) -> None:
    """Write json file.

    Args:
        file_name : str - name of the file to which data must be written
        given_data : dict - data that must be written to the file
    """
    with open(file_name, 'wt') as opened_file:
        json_data = json.dumps(given_data, indent=4)
        opened_file.write(json_data)
