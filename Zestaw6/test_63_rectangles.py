import unittest
import math
from Rectangles import Rectangle
from Points import Point

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect1 = Rectangle(0, 0, 4, 3)
        self.rect2 = Rectangle(1, -1, 5, 4)
        self.rect3 = Rectangle(0, 0, 4, 3)

    def test_str(self):
        self.assertEqual(str(self.rect1), "[(0,0),(4,3)]")
        self.assertEqual(str(self.rect2), "[(1,-1),(5,4)]")

    def test_repr(self):
        self.assertEqual(repr(self.rect1), "Rectangle(0,0,4,3)")
        self.assertEqual(repr(self.rect2), "Rectangle(1,-1,5,4)")

    def test_eq(self):
        self.assertEqual(self.rect1 == self.rect3, True)
        self.assertEqual(self.rect1 == self.rect2, False)

    def test_ne(self):
        self.assertEqual(self.rect1 != self.rect3, False)
        self.assertEqual(self.rect1 != self.rect2, True)

    def test_center(self):
        self.assertEqual(self.rect1.center(), Point(2, 1.5))
        self.assertEqual(self.rect2.center(), Point(3, 1.5))

    def test_area(self):
        self.assertEqual(self.rect1.area(), 12)
        self.assertEqual(self.rect2.area(), 20)

    def test_move(self):
        self.rect1.move(2, 1)

        self.assertEqual(self.rect1.pt1, Point(2, 1))
        self.assertEqual(self.rect1.pt2, Point(6, 4))

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy