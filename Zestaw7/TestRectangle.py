import unittest
import math
from rectangle import Rectangle
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

    def test_intersection(self): 
        inter1 = Rectangle(0, 0, 4, 4)
        inter2 = Rectangle(2, 2, 6, 6)
        expected1 = Rectangle(2, 2, 4, 4)
        self.assertEqual(inter1.intersection(inter2), expected1)

        inter3 = Rectangle(-1, 1, 4.5, 3.5)
        inter4 = Rectangle(-2, 1.5, 4, 2.1)
        expected2 = Rectangle(-1, 1.5, 4, 2.1)
        self.assertEqual(inter3.intersection(inter4), expected2)

    def test_cover(self): 
        cover1 = Rectangle(-1, 1, 4.5, 3.5)
        cover2 = Rectangle(-2, 1.5, 4, 2.1)
        expected_cover = Rectangle(-2, 1, 4.5, 3.5)
        self.assertEqual(cover1.cover(cover2), expected_cover)

    def test_make4(self):
        #test pierwszy 
        make4_rect = Rectangle(0, 0, 4, 4) 
        expected_rects = [
            Rectangle(0, 0, 2.0, 2.0),  
            Rectangle(2.0, 0, 4.0, 2.0),  
            Rectangle(0, 2.0, 2.0, 4.0),  
            Rectangle(2.0, 2.0, 4.0, 4.0)   
        ]
        self.assertEqual(make4_rect.make4(), expected_rects)

        #test 2
        make4_rect2 = Rectangle(0, 0, 6, 6)  
        expected_rects2 = [
            Rectangle(0, 0, 3.0, 3.0),  
            Rectangle(3.0, 0, 6.0, 3.0),  
            Rectangle(0, 3.0, 3.0, 6.0),  
            Rectangle(3.0, 3.0, 6.0, 6.0)   
        ]
        self.assertEqual(make4_rect2.make4(), expected_rects2)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy