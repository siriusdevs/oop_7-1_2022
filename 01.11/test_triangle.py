import pytest
from classes import Triangle, NotValidArgs

tests = [(3, 4, 5, 12), (11.5, 8, 6.34, 25.84)]


@pytest.mark.parametrize('a, b, c, perim', tests)
def test_classes_length(a, b, c, perim):
    """Прогоняет тесты по импортированной функции, проверяя периметр."""
    assert Triangle(a, b, c).perimeter() == perim


tests = [(3, 4, 5, 6), (11.5, 8, 6.34, 24.371)]


@pytest.mark.parametrize('a, b, c, area', tests)
def test_classes_area(a, b, c, area):
    """Прогоняет тесты по импортированной функции, проверяя площадь."""
    assert Triangle(a, b, c).area() == area


@pytest.mark.xfail(raises=NotValidArgs)
def test_validball():
    """Проверка отработки ошибки параметров треугольника."""
    assert Triangle(3, 10, 4).is_valid()
