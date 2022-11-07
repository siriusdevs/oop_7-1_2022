import pytest
from classes import Triangle

tests = [(3, 4, 5, 12, 6), (11.5, 8, 6.34, 25.84, 24.37086)]


@pytest.mark.parametrize('a, b, c, perim, area', tests)
def test_classes(a, b, c, perim, area):
    """Прогоняет тесты по импортированной функции."""
    assert Triangle(a, b, c).perimeter() == perim and Triangle(a, b, c).area() == area
