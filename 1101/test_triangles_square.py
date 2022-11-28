"""File with tests for triangles squares."""
import pytest
from main import Triangle

triangle_square_data = [(3, 4, 5, 6.0), (2, 2, 3, 1.98)]


@pytest.mark.parametrize('first, second, third, square', triangle_square_data)
def test_perimeter(first, second, third, square):
    """Function tests square method from class Triangle.

    Args:
        first: int - first side.
        second: int - second side.
        third: int - third side.
        square: float - work result.
    """
    assert Triangle(first, second, third).square() == square
