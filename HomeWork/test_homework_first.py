"""Testing file."""
import pytest
from homework_first import Circle, Triangle, NonexistentFigure


test_triangle_first = [
    (['два', 1, 4], False), (["...", 7, 5], False), ([6, 0, 5], False), ([-3, 4, 5], False)
]


@pytest.mark.xfail(raises=NonexistentFigure)
@pytest.mark.parametrize('sides, expectation', test_triangle_first)
def test_trinagle_first(sides, expectation):
    """Test not valid triangle.

    Args:
        sides (List[float]): sides of trinagle.
        expectation (bool): what we expect.
    """
    assert Triangle(sides).isvalid() == expectation


test_circle_first = [("nine", False), (-9, False)]


@pytest.mark.xfail(raises=NonexistentFigure)
@pytest.mark.parametrize('radius, expectation', test_circle_first)
def test_first_circle(radius, expectation):
    """Test not valid circle."""
    assert Circle(radius).isvalid() == expectation


test_triangle_second = [([7.0, 5.0, 4.0], True), ([3.0, 3.0, 3.0], True), ([10.0, 8.0, 10.0], True)]


@pytest.mark.xfail(raises=NonexistentFigure)
@pytest.mark.parametrize('sides, expectation', test_triangle_second)
def test_trinagle_second(sides, expectation):
    """Test not valid triangle.

    Args:
        sides (List[float]): sides jf trinagle.
        expectation (bool): what we expect.
    """
    assert Triangle(sides).isvalid() == expectation


test_circle_second = [(6.0, True), (5.0, True), (3.0, True), (-1.0, False)]


@pytest.mark.xfail(raises=NonexistentFigure)
@pytest.mark.parametrize('radius, expectation', test_circle_second)
def test_second_circle(radius, expectation):
    """Test not valid circle."""
    assert Circle(radius).isvalid() == expectation


test_triangle_third = [[4.0, 4.0, 4.0], [10.0, 8.0, 10.0]]


@pytest.mark.parametrize('sides', test_triangle_third)
def test_trinagle_third(sides):
    """Test for triangle's sides.

    Args:
        sides (List[float]): sides of trinagle.
    """
    triangle = Triangle(sides)
    assert triangle.first_side == sides[0]
    assert triangle.second_side == sides[1]
    assert triangle.third_side == sides[2]


test_circle_third = [(9.0), (8.0), (7.0)]


@pytest.mark.parametrize('radius', test_circle_third)
def test_rhird_circle(radius):
    """Test for circle's radius.

    Args:
        radius (float): circle's radius.
    """
    assert Circle(radius).radius == radius


test_triangle_fourth = [([4.0, 4.0, 4.0], 12.0), ([1.1, 2.2, 3.3], 6.6)]


@pytest.mark.parametrize('sides, wait', test_triangle_fourth)
def test_perimeter_fourth(sides, wait):
    """Test for triangle's perimeter.

    Args:
        sides (List[float]): sides of trinagle.
    """
    assert Triangle(sides).perimeter() == wait


test_triangle_fifth = [([4.0, 4.0, 4.0], 6.928), ([10.0, 8.0, 10.0], 36.661)]


@pytest.mark.parametrize('sides, wait', test_triangle_fifth)
def test_trinagle_fifth(sides, wait):
    """Test for triangle's square.

    Args:
        sides (List[float]): sides of trinagle.
    """
    assert Triangle(sides).area() == wait


test_circle_fourth = [(3.0, 18.85), (6.0, 37.699)]


@pytest.mark.parametrize('radius, wait', test_circle_fourth)
def test_fourth_circle(radius, wait):
    """Test for circumference.

    Args:
        radius (float): circle's radius.
    """
    assert Circle(radius).circumference() == wait


test_circle_fifth = [(3.0, 28.274), (6.0, 113.097)]


@pytest.mark.parametrize('radius, wait', test_circle_fifth)
def test_fifth_circle(radius, wait):
    """Test for circle's area.

    Args:
        radius (float): circle's radius.
    """
    assert Circle(radius).area() == wait
