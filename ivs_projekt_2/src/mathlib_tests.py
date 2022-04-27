# mathlib_tests.py
# Author: Filip Spacek
# Login: xspace38
# Date; 27-04-2022

import unittest

from src.mathlib import MathLibrary

#ADDITION TESTS
class Addition_lib_test(unittest.TestCase):
    def setUp(self):
        self.math = MathLibrary

    #testing addition of positive numbers
    def Addition_test_positive(self):
        self.assertEqual(self.math.add(3, 5), 8)
        self.assertEqual(self.math.add(9, 2), 11)
        self.assertEqual(self.math.add(0, 0), 0)
        self.assertEqual(self.math.add(0, 1), 1)
        self.assertEqual(self.math.add(1, 0), 1)

    #testing addition of negative numbers
    def Addition_test_negative(self):
        self.assertEqual(self.math.add(0, -5), -5)
        self.assertEqual(self.math.add(-3, 0), -3)
        self.assertEqual(self.math.add(3, -2), 1)
        self.assertEqual(self.math.add(-2, 1), -1)
        self.assertEqual(self.math.add(-4, -6), -10)

    #testing addition of decimal numbers
    def Addition_test_dec(self):
        self.assertEqual(self.math.add(0, 0.55), 0.55)
        self.assertEqual(self.math.add(0.44, 0), 0.44)
        self.assertEqual(self.math.add(0.5, -0.25), 0.25)
        self.assertEqual(self.math.add(-2.6, 3), 0.4)
        self.assertEqual(self.math.add(-4.5, -6.7), -11.2)
        self.assertEqual(self.math.add(0.333, 0.444), 0.777)

#SUBSTRACTION TESTS
class Substraction_lib_test(unittest.TestCase):
    def setUp(self):
        self.math = MathLibrary

    #testing substraction of positive numbers
    def Substraction_test_positive(self):
        self.assertEqual(self.math.subtract(0, 0), 0)
        self.assertEqual(self.math.subtract(0, 4), -4)
        self.assertEqual(self.math.subtract(84, 0), -84)
        self.assertEqual(self.math.subtract(9, 4), 5)
        self.assertEqual(self.math.subtract(4, 9), -5)

    #testing substraction of negative numbers
    def Substraction_test_negative(self):
        self.assertEqual(self.math.subtract(0, -4), 4)
        self.assertEqual(self.math.subtract(-84, 0), 84)
        self.assertEqual(self.math.subtract(-9, 4), -13)
        self.assertEqual(self.math.subtract(4, -9), 13)
        self.assertEqual(self.math.subtract(-95, -11), -84)

    #testing substraction of decimal numbers
    def Substraction_test_dec(self):
        self.assertEqual(self.math.subtract(0, 4.5), -4.5)
        self.assertEqual(self.math.subtract(4.5, 0), 4.5)
        self.assertEqual(self.math.subtract(4.1, 0.1), 4)
        self.assertEqual(self.math.subtract(4.1, 0.6), 3.5)
        self.assertEqual(self.math.subtract(0.334, 0.223), 0.111)
        self.assertEqual(self.math.subtract(-4.1, 0.7), -4.8)
        self.assertEqual(self.math.subtract(4.1, -0.7), 4.8)
        self.assertEqual(self.math.subtract(-4.1, -0.7), -3.4)

#DIVISION TESTS
class Division_lib_test(unittest.TestCase):
    def setUp(self):
        self.math = MathLibrary

    #testing division by zero -> u shouldn't divide by zero
    #assertraises to throw an exception
    def Division_test_zero(self):
        with self.assertRaises(ValueError):
            self.math.divide(343, 0)

    #testing division for positive numbers
    def Division_test_positive(self):
        self.assertEqual(self.math.divide(3, 3), 1)
        self.assertEqual(self.math.divide(8, 4), 2)
        self.assertEqual(self.math.divide(4, 8), 0.5)
        self.assertEqual(self.math.divide(1000, 10), 100)

    #testing division for negative numbers
    def Division_test_negative(self):
        self.assertEqual(self.math.divide(-6, 2), -3)
        self.assertEqual(self.math.divide(16, -4), -4)
        self.assertEqual(self.math.divide(-1450, -50), 29)
        self.assertEqual(self.math.divide(-3, 10), -0.3)
        self.assertEqual(self.math.divide(3, -10), -0.3)

    #testing division for decimal numbers
    def Division_test_dec(self):
        self.assertEqual(self.math.divide(0.85, 0.5), 1.7)
        self.assertEqual(self.math.divide(0.06, 0.12), 0.5)
        self.assertEqual(self.math.divide(4.8, 2.4), 2)
        self.assertEqual(self.math.divide(-4.4, 0.4), -11)
        self.assertEqual(self.math.divide(0.45, -0.5), 0.9)
        self.assertEqual(self.math.divide(-3.3, -6.6), 0.5)

#MULTIPLICATION TESTS
class Multiplication_lib_test(unittest.TestCase):
    def setUp(self):
        self.math = MathLibrary

    #testing multiplication by positive numbers and zero
    def Multiplication_test_positive(self):
        self.assertEqual(self.math.multiply(0, 0), 0)
        self.assertEqual(self.math.multiply(4, 0), 0)
        self.assertEqual(self.math.multiply(0, 80), 0)
        self.assertEqual(self.math.multiply(6, 8), 48)
        self.assertEqual(self.math.multiply(48, 2), 96)
        self.assertEqual(self.math.multiply(48, 48), 2304)

    #testing multiplication by negative numbers
    def Multiplication_test_negative(self):
        self.assertEqual(self.math.multiply(-46, 31), -1426)
        self.assertEqual(self.math.multiply(24, -33), -792)
        self.assertEqual(self.math.multiply(-32, -64), 2048)

    #testing multiplication by decimal numbers
    def Multiplication_test_dec(self):
        self.assertEqual(self.math.multiply(4, 4.8), 19.2)
        self.assertEqual(self.math.multiply(2.44, 6), 14.64)
        self.assertEqual(self.math.multiply(4.3, 12.6), 54.18)
        self.assertEqual(self.math.multiply(-8.4, 4.6), -38.64)
        self.assertEqual(self.math.multiply(4.32, -8.45), -36.504)
        self.assertEqual(self.math.multiply(-4.4, -19.33), 85.052)
        self.assertEqual(self.math.multiply(0.123, 0.456), 0.056088)


if __name__ == '__main__':
    unittest.main()