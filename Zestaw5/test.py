import unittest
import main5

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        #assertEqual compares returned value from add_frac fuunction with the expected value (5/6)
        self.assertEqual(main5.add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(main5.add_frac([-2, 8], [-4, 8]), [-3, 4])

    def test_sub_frac(self):
        self.assertEqual(main5.sub_frac([-2, 8], [-4, 8]), [1, 4])
        self.assertEqual(main5.sub_frac([7, 8], [5, 3]), [-19, 24])

    def test_mul_frac(self):
        self.assertEqual(main5.mul_frac([7, 8], [5, 3]), [35, 24])
        self.assertEqual(main5.mul_frac([9, 2], [3, 6]), [9, 4])

    def test_div_frac(self):
        self.assertEqual(main5.div_frac([3, 5], [1, 4]), [12, 5])
        self.assertEqual(main5.div_frac([33, 13], [11, 5]), [15, 13])

    def test_is_positive(self):
        self.assertEqual(main5.is_positive([33, 13]), True)
        self.assertEqual(main5.is_positive([1, -3]), False)
        self.assertEqual(main5.is_positive([-1, -3]), True)
    def test_is_zero(self):
        self.assertEqual(main5.is_zero([0, 1]), True)
        self.assertEqual(main5.is_zero([1, 1]), False)

    def test_cmp_frac(self):
        self.assertEqual(main5.cmp_frac([3, 6], [1, 2]), 0)
        self.assertEqual(main5.cmp_frac([5, 3], [4, 3]), 1)
        self.assertEqual(main5.cmp_frac([1, 4], [1, 2]), -1)
        self.assertEqual(main5.cmp_frac([-3, 4], [-1, 2]), -1)
        self.assertEqual(main5.cmp_frac([-1, 4], [-3, 4]), 1)

    def test_frac2float(self):
        self.assertEqual(main5.frac2float([1, 1000000]), 0.000001)
        self.assertEqual(main5.frac2float([123456789, 10000000]), 12.3456789)
        self.assertEqual(main5.frac2float([-3, 4]), -0.75)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy