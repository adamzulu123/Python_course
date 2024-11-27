#testy dla rectangle
import pytest
from Points import Point
from rectangle import Rectangle

@pytest.fixture(name='rectangle')
def rectangle():
    return Rectangle(1, 1, 3, 5)

def test_form_points(rectangle):
    points = [Point(1, 1), Point(3, 5)]
    rect = Rectangle.from_points(points)
    assert rect == rectangle

def test_center(rectangle):
    assert rectangle.center == Point(2, 3)

def test_top_bottom_right_left(rectangle):
    assert rectangle.bottom == 1
    assert rectangle.top == 5
    assert rectangle.left == 1
    assert rectangle.right == 3

def test_width_height(rectangle):
    assert rectangle.width == 2
    assert rectangle.height == 4

def test_all_points(rectangle):
    assert rectangle.bottom_left == Point(1,1)
    assert rectangle.bottom_right == Point(3,1)
    assert rectangle.top_left == Point(1,5)
    assert rectangle.top_right == Point(3,5)

def test_area(rectangle):
    assert rectangle.area() == 8

def test_cover(rectangle):
    other_rectangle = Rectangle(2, 3, 4, 7)
    assert rectangle.cover(other_rectangle) == Rectangle(1,1,4,7)

def test_make4(rectangle):
    # Rectangle(1, 1, 3, 5)
    new_rectangles = rectangle.make4()
    assert new_rectangles[0] == Rectangle(1, 1, 2, 3)
    assert new_rectangles[1] == Rectangle(2, 1, 3, 3)
    assert new_rectangles[2] == Rectangle(1, 3, 2, 5)
    assert new_rectangles[3] == Rectangle(2, 3, 3, 5)
