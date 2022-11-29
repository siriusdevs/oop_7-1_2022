import pytest
from circle import Circle

tests_create_circle = [4.0, 2, 1.5]


@pytest.mark.parametrize('radius', tests_create_circle)
def test_circle_create(radius: float or int) -> None:
    """
    Test for create circle.
    Тесты создания окружности.
    Args:
        radius: float - radius of the circle.
        десятичное число - радиус окружности.
    """
    circle = Circle(radius)
    assert circle.radius == radius


@pytest.mark.xfail(raises=ValueError)
def test_invalid_circle_create():
    """
    Tests for raises circles exeption ValueError.
    Тесты для вызова ошибок ValueError у окружностей
    """
    with pytest.raises(ValueError):
        Circle(-1)

    with pytest.raises(ValueError):
        Circle(0)

    with pytest.raises(ValueError):
        Circle("2")


tests_length = [(Circle(1), 6.28), (Circle(2.25), 14.14)]


@pytest.mark.parametrize("circle, expect", tests_length)
def tests_to_find_length(circle: Circle, expect: float) -> None:
    """
    Tests for the correct calculation of the length of a circle.
    Тесты на правильность подсчёта длины окружности.
    """
    assert circle.get_circle_length() == expect


tests_square = [(Circle(1), 3.14), (Circle(2.25), 15.9)]


@pytest.mark.parametrize("circle, expect", tests_square)
def tests_to_find_square(circle: Circle, expect: float) -> None:
    """
    Tests for the correct calculation of the square of a circle.
    Тесты на правильность подсчёта площади окружности.
    """
    assert circle.get_circle_square() == expect
