import pytest
from classes import Circle


tests = [(1, 6.28319, 3.14159), (55.88, 351.10439, 9809.8568)]


@pytest.mark.parametrize('r, length, area', tests)
def test_classes(r, length, area):
    """Прогоняет тесты по импортированной функции."""
    assert Circle(r).length() == length and Circle(r).area() == area
