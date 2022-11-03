import pytest
from main import Round

test_square_data = [(2, 12.57), (5, 78.54)]


@pytest.mark.parametrize('radius, answer', test_square_data)
def test_square(radius, answer):
    """Function tests round method - square.

    Args:
        radius: int - input radius.
        answer: float - work result.
    """
    assert Round(radius).square() == answer
