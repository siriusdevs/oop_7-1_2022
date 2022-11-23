"""Testing file."""
import pytest
from HW_01 import Circle, Triangle, NoneExistentFigure


test_triangle1 = [(['два', 1, 4], False), (["...", 7, 5], False), ([6, "yeet", 5], False), ([-3, 4, 5], False)]


@pytest.mark.xfail(raises=NoneExistentFigure)
@pytest.mark.parametrize('sides, expectation', test_triangle1)
def test_trinagle_1(sides, expectation):
    """Test not valid triangle.
    Args:
        sides List[float]: sides of trinagle.
        expectation (bool): what we expect.
    """
    assert Triangle(sides).isvalid(sides) == expectation


test_circle1 = [("nine", False), (-9, False)]


@pytest.mark.xfail(raises=NoneExistentFigure)
@pytest.mark.parametrize('radius, expectation', test_circle1)
def test_circle_2(radius, expectation):
    assert Circle(radius).isvalid(radius) == expectation


test_triangle2 = [([7.0, 5.0, 4.0], True), ([3.0, 3.0, 3.0], True), ([10.0, 8.0, 10.0], True)]


@pytest.mark.xfail(raises=NoneExistentFigure)
@pytest.mark.parametrize('sides, expectation', test_triangle2)
def test_trinagle_2(sides, expectation):
    """Test not valid triangle.
    Args:
        sides List[float]: sides jf trinagle.
        expectation (bool): what we expect.
    """
    assert Triangle(sides).isvalid(sides) == expectation


test_circle2 = [(6.0, True), (5.0, True), (3.0, True), (-1.0, False)]


@pytest.mark.xfail(raises=NoneExistentFigure)
@pytest.mark.parametrize('radius, expectation', test_circle2)
def test_circle_2(radius, expectation):
    assert Circle(radius).isvalid(radius) == expectation


test_triangle_3 = [[4.0, 4.0, 4.0], [10.0, 8.0, 10.0]]


@pytest.mark.parametrize('sides', test_triangle_3)
def test_triangle_3(sides):
    """Test for triangle's sides.
    Args:
        sides List(float): sides of trinagle.
    """
    triangle = Triangle(sides)
    assert triangle.side_1 == sides[0]
    assert triangle.side_2 == sides[1]
    assert triangle.side_3 == sides[2]


test_circle_3 = [(9.0), (8.0), (7.0)]


@pytest.mark.parametrize('radius', test_circle_3)
def test_circle_3(radius):
    """Test for circle's radius.
    Args:
        radius (float): circle's radius.
    """
    assert Circle(radius).radius == radius


test_triangle_4 = [([4.0, 4.0, 4.0], 12.0), ([1.1, 2.2, 3.3], 6.6)]


@pytest.mark.parametrize('sides, wait', test_triangle_4)
def test_perimeter_4(sides, wait):
    """Test for triangle's perimeter.
    Args:
        sides List(float): sides of trinagle.
        expect (float): triangle's perimeter.
    """
    assert Triangle(sides).perimeter() == wait


test_triangle_5 = [([4.0, 4.0, 4.0], 6.928), ([10.0, 8.0, 10.0], 36.661)]


@pytest.mark.parametrize('sides, wait', test_triangle_5)
def test_trinagle_5(sides, wait):
    """Test for triangle's square.
    Args:
        sides List(float): sides of trinagle.
        expect (float): triangle's square.
    """
    assert Triangle(sides).area() == wait


test_circle_4 = [(3.0, 18.85), (6.0, 37.699)]


@pytest.mark.parametrize('radius, wait', test_circle_4)
def test_circle_4(radius, wait):
    """Test for circumference.
    Args:
        radius (float): circle's radius.
        expect (float): circumference.
    """
    assert Circle(radius).circumference() == wait


test_circle_5 = [(3.0, 28.274), (6.0, 113.097)]


@pytest.mark.parametrize('radius, wait', test_circle_5)
def test_circle_5(radius, wait):
    """Test for circle's area.
    Args:
        radius (float): circle's radius.
        expect (float): circle's area.
    """
    assert Circle(radius).area() == wait