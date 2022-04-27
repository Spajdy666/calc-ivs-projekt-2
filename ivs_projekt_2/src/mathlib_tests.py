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