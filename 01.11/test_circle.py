import pytest
from classes import Circle, NotValidArgs


tests = [(1, 6.283), (55.88, 351.104)]


@pytest.mark.parametrize('r, length', tests)
def test_classes_length(r, length):
    """Прогоняет тесты по импортированной функции, проверяя длину окружности."""
    assert Circle(r).length() == length


tests = [(1, 3.142), (55.88, 9809.857)]


@pytest.mark.parametrize('r, area', tests)
def test_classes_area(r, area):
    """Прогоняет тесты по импортированной функции, проверяя площадь."""
    assert Circle(r).area() == area


@pytest.mark.xfail(raises=NotValidArgs)
def test_validball():
    """Проверка отработки ошибки параметров круга."""
    assert Circle(-2).is_valid()
