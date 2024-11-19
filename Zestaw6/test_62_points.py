import unittest
import math
from Points import Point

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.zero = Point(0, 0)

    def test_str(self):
        self.assertEqual(str(Point(3,2)), "(3,2)")
        self.assertEqual(str(Point(12.7,3.69)), "(12.7,3.69)")

    def test_repr(self):
        self.assertEqual(repr(Point(12.7, 3.69)), "Point(12.7,3.69)")

    def test_eg(self):
        self.assertEqual(Point(3,2) == Point(3,2), True)
        self.assertEqual(Point(12.7,1) == Point(12.7,3.69), False)

    def test_neq(self):
        self.assertEqual(Point(3,2) != Point(3,3), True)

    def test_add(self):
        self.assertEqual(Point(3,2) + Point(3,2), Point(6,4))
        self.assertEqual(Point(3.4, 2.1) + Point(3.1, 2.1), Point(6.5, 4.2))

    def test_sub(self):
        self.assertEqual(Point(3, 2) - Point(0, 2), Point(3, 0))
        self.assertEqual(Point(10.5,2.3) - Point(5,2.3), Point(5.5,0))

    def test_mul(self):
        self.assertEqual(Point(3,2) * Point(3,2), 13)
        self.assertEqual(Point(5, 5) * Point(5, 5), 50)

    def test_cross(self):
        self.assertEqual(Point(3,2).cross(Point(3,2)), 0)
        self.assertEqual(Point(3,2).cross(Point(0,2)), 6)

    def test_length(self):
        self.assertEqual(Point(3, 2).length(), math.sqrt(13))
        self.assertEqual(Point(65.4, 2).length(), math.sqrt(65.4**2 + 2**2))

    def test_hash(self):
        self.assertEqual(hash(Point(3,2)), hash(Point(3,2)))

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
