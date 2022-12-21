"""Tests for json functions."""
from additional_functions.json_func import read_json
from conf_test import MAP1_A, MAP2_A, MAP3_A
import pytest


case1 = {'MAP1_A': MAP1_A}
case2 = {'MAP2_A': MAP2_A}
case3 = {'MAP3_A': MAP3_A}
tests_read = [
    ('json_test_cases/read1.json', case1),
    ('json_test_cases/read2.json', case2),
    ('json_test_cases/read3.json', case3)
]


@pytest.mark.parametrize('file_name, output_dict', tests_read)
def test_json_read(file_name: str, output_dict: dict) -> None:
    """Test reading from json file."""
    assert read_json(file_name) == output_dict
