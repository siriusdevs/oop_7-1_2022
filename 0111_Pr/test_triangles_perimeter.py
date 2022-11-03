"""File with tests for triangles perimeter."""
import pytest
from main import Triangle

triangle_perimeter_data = [(3, 4, 5, 12), (2, 2, 3, 7)]


@pytest.mark.parametrize('first, second, third, perimeter', triangle_perimeter_data)
def test_perimeter(first, second, third, perimeter):
    """Function tests perimeter method from class Triangle.

    Args:
        first: int - first side.
        second: int - second side.
        third: int - third side.
        perimeter: int - work result.
    """
    assert Triangle(first, second, third).perimeter() == perimeter
