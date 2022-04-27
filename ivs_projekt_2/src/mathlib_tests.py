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
    def test_Addition_positive(self):
        self.assertEqual(self.math.add(3, 5), 8)
        self.assertEqual(self.math.add(9, 2), 11)
        self.assertEqual(self.math.add(0, 0), 0)
        self.assertEqual(self.math.add(0, 1), 1)
        self.assertEqual(self.math.add(1, 0), 1)

    #testing addition of negative numbers
    def test_Addition_negative(self):
        self.assertEqual(self.math.add(0, -5), -5)
        self.assertEqual(self.math.add(-3, 0), -3)
        self.assertEqual(self.math.add(3, -2), 1)
        self.assertEqual(self.math.add(-2, 1), -1)
        self.assertEqual(self.math.add(-4, -6), -10)

    #testing addition of decimal numbers
    def test_Addition_dec(self):
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
    def test_Substraction_positive(self):
        self.assertEqual(self.math.subtract(0, 0), 0)
        self.assertEqual(self.math.subtract(0, 4), -4)
        self.assertEqual(self.math.subtract(84, 0), -84)
        self.assertEqual(self.math.subtract(9, 4), 5)
        self.assertEqual(self.math.subtract(4, 9), -5)

    #testing substraction of negative numbers
    def test_Substraction_negative(self):
        self.assertEqual(self.math.subtract(0, -4), 4)
        self.assertEqual(self.math.subtract(-84, 0), 84)
        self.assertEqual(self.math.subtract(-9, 4), -13)
        self.assertEqual(self.math.subtract(4, -9), 13)
        self.assertEqual(self.math.subtract(-95, -11), -84)

    #testing substraction of decimal numbers
    def test_Substraction_dec(self):
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
    def test_Division_zero(self):
        with self.assertRaises(ValueError):
            self.math.divide(343, 0)

    #testing division for positive numbers
    def test_Division_positive(self):
        self.assertEqual(self.math.divide(3, 3), 1)
        self.assertEqual(self.math.divide(8, 4), 2)
        self.assertEqual(self.math.divide(4, 8), 0.5)
        self.assertEqual(self.math.divide(1000, 10), 100)

    #testing division for negative numbers
    def test_Division_negative(self):
        self.assertEqual(self.math.divide(-6, 2), -3)
        self.assertEqual(self.math.divide(16, -4), -4)
        self.assertEqual(self.math.divide(-1450, -50), 29)
        self.assertEqual(self.math.divide(-3, 10), -0.3)
        self.assertEqual(self.math.divide(3, -10), -0.3)

    #testing division for decimal numbers
    def test_Division_dec(self):
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
    def test_Multiplication_positive(self):
        self.assertEqual(self.math.multiply(0, 0), 0)
        self.assertEqual(self.math.multiply(4, 0), 0)
        self.assertEqual(self.math.multiply(0, 80), 0)
        self.assertEqual(self.math.multiply(6, 8), 48)
        self.assertEqual(self.math.multiply(48, 2), 96)
        self.assertEqual(self.math.multiply(48, 48), 2304)

    #testing multiplication by negative numbers
    def test_Multiplication_negative(self):
        self.assertEqual(self.math.multiply(-46, 31), -1426)
        self.assertEqual(self.math.multiply(24, -33), -792)
        self.assertEqual(self.math.multiply(-32, -64), 2048)

    #testing multiplication by decimal numbers
    def test_Multiplication_dec(self):
        self.assertEqual(self.math.multiply(4, 4.8), 19.2)
        self.assertEqual(self.math.multiply(2.44, 6), 14.64)
        self.assertEqual(self.math.multiply(4.3, 12.6), 54.18)
        self.assertEqual(self.math.multiply(-8.4, 4.6), -38.64)
        self.assertEqual(self.math.multiply(4.32, -8.45), -36.504)
        self.assertEqual(self.math.multiply(-4.4, -19.33), 85.052)
        self.assertEqual(self.math.multiply(0.123, 0.456), 0.056088)

#FACTORIAL TESTS
class Factorial_lib_test(unittest.TestCase):
    def setUp(self):
        self.math = MathLibrary

    #testing factorials that cannot be solved
    def test_Factorial_positive(self):
        #negative numbers
        with self.assertRaises(ValueError):
            self.math.fact(-1)
        with self.assertRaises(ValueError):
            self.math.fact(-3)
        with self.assertRaises(ValueError):
            self.math.fact(-8)
        #decimal numbers
        with self.assertRaises(ValueError):
            self.math.fact(4.5)
        with self.assertRaises(ValueError):
            self.math.fact(0.33333)
        with self.assertRaises(ValueError):
            self.math.fact(-4.271)

    #testing factorial for zero -> 0! == 1
    def test_Factorial_zero(self):
        self.assertEqual(self.math.fact(0), 1)

    #testing valid factorials
    def test_Factorial(self):
        self.assertEqual(self.math.fact(5), 120)
        self.assertEqual(self.math.fact(1), 1)
        self.assertEqual(self.math.fact(8), 40320)

#POWER TESTS
class Power_lib_test(unittest.TestCase):
    def setUp(self):
        self.math = MathLibrary

    #exponent should be positive
    def test_Power_negative_exponent(self):
        with self.assertRaises(ValueError):
            self.math.power(3, -1)
        with self.assertRaises(ValueError):
            self.math.power(8, -5)

    #exponent is zero, the result is 1 by definition
    def test_Power_zero(self):
        self.assertEqual(self.math.power(67, 0), 1)
        self.assertEqual(self.math.power(43, 0), 1)

    #power for positive numbers
    def test_Power_positive(self):
        self.assertEqual(self.math.power(5, 1), 5)
        self.assertEqual(self.math.power(7, 3), 343)
        self.assertEqual(self.math.power(3, 10), 59049)

    #power for negative numbers
    def test_Power_negative(self):
        self.assertEqual(self.math.power(-4, 2), 16)
        self.assertEqual(self.math.power(-5, 3), -125)
        self.assertEqual(self.math.power(-16, 4), 65536)
        self.assertEqual(self.math.power(-4, 5), -1024)

    #power for decimal numbers
    def test_Power_dec(self):
        self.assertEqual(self.math.power(2.2, 5), 51.53632)
        self.assertEqual(self.math.power(1.1, 2), 1.21)
        self.assertEqual(self.math.power(-1.1, 2), 1.21)
        self.assertEqual(self.math.power(-1.1, 3), -1.331)

#ROOT TESTS
class Root_lib_test(unittest.TestCase):
    def setUp(self):
        self.math = MathLibrary

    #root exponent isn't negative/decimal/zero
    def test_Root_invalid_exponent(self):
        with self.assertRaises(ValueError):
            self.math.root(4, -3)
        with self.assertRaises(ValueError):
            self.math.root(3, -15)
        with self.assertRaises(ValueError):
            self.math.root(2, 0)
        with self.assertRaises(ValueError):
            self.math.root(3, 1.15)

    #root for positive numbers
    def test_Root_positive(self):
        self.assertEqual(self.math.root(4, 2), 2)
        self.assertEqual(self.math.root(27, 3), 3)
        self.assertAlmostEqual(self.math.root(26, 4), 2.2581)

    #root for decimal numbers
    def test_Root_dec(self):
        self.assertAlmostEqual(self.math.root(1.6, 1.25), 1.4564513624209)
        self.assertAlmostEqual(self.math.root(3.6, 4.1), 1.3667325471843)
        self.assertAlmostEqual(self.math.root(2.5, 5.75), 1.172754094857)

#LN TESTS
class Ln_lib_test(unittest.TestCase):
    def setUp(self):
        self.math = MathLibrary

    #invalid numbers for ln -> zero and negative numbers
    def test_Ln_invalid(self):
        with self.assertRaises(ValueError):
            self.math.ln(0)
        with self.assertRaises(ValueError):
            self.math.ln(-3)
        with self.assertRaises(ValueError):
            self.math.ln(-5)

    #ln of number 1
    def test_Ln_one(self):
        self.assertEqual(self.math.ln(1), 0)

    #ln of positive numbers
    def test_Ln_positive(self):
        self.assertAlmostEqual(self.math.ln(5), 1.6094379124341003)
        self.assertAlmostEqual(self.math.ln(3), 1.0986122886681096)
        self.assertAlmostEqual(self.math.ln(11), 2.3978952727983707)

    #ln of decimal numbers
    def test_Ln_dec(self):
        self.assertAlmostEqual(self.math.ln(3.6), 1.2809338454620645)
        self.assertAlmostEqual(self.math.ln(8.125), 2.094945728215801)
        self.assertAlmostEqual(self.math.ln(12.445), 2.521318935819555)

if __name__ == '__main__':
    unittest.main()