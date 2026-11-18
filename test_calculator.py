import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3,1), 3)
        self.assertEqual(mul(4,2), 8)
        self.assertEqual(mul(10, -10), -100)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(9, 3), 3)
        self.assertEqual(div(121, -11), -11)
        self.assertEqual(div(-26, -13), 2)

    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
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

# Do not touch this
if __name__ == "__main__":
    unittest.main()