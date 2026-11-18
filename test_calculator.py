# https://github.com/Dominik-DiBenedetto/lab11-DD-GN
# Partner 1: Gavin Nazal
# Partner 2: Dominik DiBenedetto

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3,1), 3)
        self.assertEqual(mul(4,2), 8)
        self.assertEqual(mul(10, -10), -100)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(3, 9), 3)
        self.assertEqual(div(-11, 121), -11)
        self.assertEqual(div(-13, -26), 2)

    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5,0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(6, 8), 10)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-10)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(16), 4)

    def test_add(self): # 3 assertions
        self.assertEqual(add(1,1), 2)
        self.assertEqual(add(-1,1), 0)
        self.assertEqual(add(10,0), 10)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(1,1), 0)
        self.assertEqual(subtract(-1,1), -2)
        self.assertEqual(subtract(10,2), 8)

    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2,8), 3)
        self.assertEqual(logarithm(3,81), 4)
        self.assertEqual(logarithm(4,1), 0)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(0, 5)

# Do not touch this
if __name__ == "__main__":
    unittest.main()