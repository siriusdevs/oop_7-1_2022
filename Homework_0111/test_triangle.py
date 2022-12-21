"""Testing circles_and_triangles. Class Triangle."""
from circles_and_triangles import Triangle, STerr
import pytest


triangle_ptrs = [(2, 7, 6), (1.8, 3.2, 4.7), (2, 2.3, 4)]


@pytest.mark.parametrize('first_side, second_side, third_side', triangle_ptrs)
def test_circle_ptrs(first_side: float, second_side: float, third_side: float) -> None:
    """Test for param of elements of class Triangle.

    Args:
        first_side : float - first side of triangle.
        second_side : float - second side of triangle.
        third_side : float - third side of triangle.
    """
    assert Triangle(first_side, second_side, third_side).first_side == first_side
    assert Triangle(first_side, second_side, third_side).second_side == second_side
    assert Triangle(first_side, second_side, third_side).third_side == third_side


@pytest.mark.xfail(raises=STerr)
def test_circle_valid():
    """Tests for triangles' STerr."""
    with pytest.raises(STerr):
        assert Triangle(1, 1, 3)


tests_valid = [((2.5, 1, 3), True), ((2, 3, 4), True)]


@pytest.mark.parametrize('sides, res', tests_valid)
def test_is_valid(sides: tuple, res: bool):
    """Test for attributes for an obj of class Triangle.

    Args:
        sides: tuple - tuple with sides of a triangle.
        res: bool - acceptable attribute or not.
    """
    assert Triangle(sides[0], sides[1], sides[2]).is_valid() == res


triangle_area = [((1, 7, 7), 3.491), ((3.2, 1.2, 4), 1.587)]


@pytest.mark.parametrize('sides, res', triangle_area)
def test_area_tr(sides: tuple, res: float) -> None:
    """Test for area of a triangle.

    Args:
        sides: tuple - tuple with sides of a triangle.
        res: float - area of triangle.
    """
    assert Triangle(sides[0], sides[1], sides[2]).area() == res


triangle_per = [((2, 7, 6), 15), ((2, 2.3, 4), 8.3)]


@pytest.mark.parametrize('sides, res', triangle_per)
def test_per_tr(sides: tuple, res: float) -> None:
    """Test for perimeter of a triangle.

    Args:
        sides: tuple - tuple with sides of a triangle.
        res: float - perimeter of triangle.
    """
    assert Triangle(sides[0], sides[1], sides[2]).perimeter() == res
