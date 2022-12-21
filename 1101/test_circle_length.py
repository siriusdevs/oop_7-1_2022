import pytest
from main import Circle

test_length_data = [(2, 12.57), (5, 31.42)]


@pytest.mark.parametrize('radius, answer', test_length_data)
def test_length(radius, answer):
    """Function tests round method - length.

    Args:
        radius: int - input radius.
        answer: float - work result.
    """
    assert Circle(radius).length() == answer
