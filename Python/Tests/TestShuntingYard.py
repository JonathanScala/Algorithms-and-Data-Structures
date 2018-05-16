import unittest
import sys
import os


class TestConvertMethod(unittest.TestCase):

    def test_basic_addition(self):
        result = PostFix.convert('x+y')
        self.assertEqual(result, 'xy+', "Cannot add two variables")

    def test_basic_subtraction(self):
        result = PostFix.convert('x-y')
        self.assertEqual(result, 'xy-', "Cannot subtract two variables")

    def test_basic_multiplication(self):
        result = PostFix.convert('x*y')
        self.assertEqual(result, 'xy*', "Cannot Multiply two variables")

    def test_basic_multiplication(self):
        result = PostFix.convert('x/y')
        self.assertEqual(result, 'xy/', "Cannot Multiply two variables")

    def test_division_and_subtraction(self):
        result = PostFix.convert('(x)/(y-z)')
        self.assertEqual(result, 'xyz-/',
                         "Cannot Divide and Subtract Simultaneously")

    def test_division_and_Multiplication(self):
        result = PostFix.convert('(x)/(y*z)')
        self.assertEqual(result, 'xyz*/',
                         "Cannot Divide and Multiply Simultaneously")

    def test_division_and_Addition(self):
        result = PostFix.convert('(x)/(y+z)')
        self.assertEqual(result, 'xyz+/',
                         "Cannot Divide and Add Simultaneously")

    def test_Multiplication_and_Subtraction(self):
        result = PostFix.convert('x*(y-z)')
        self.assertEqual(result, 'xyz-*',
                         "Cannot Multiply and Subtract Simultaneously")

    def test_Multiplication_and_Addition(self):
        result = PostFix.convert('x*(y+z)')
        self.assertEqual(result, 'xyz+*',
                         "Cannot Multiply and Add Simultaneously")

    def test_Addition_and_Subtraction(self):
        result = PostFix.convert('x+(y-z)')
        self.assertEqual(result, 'xyz-+',
                         "Cannot Add and Subtract Simultaneously")

    def test_all_operators(self):
        result = PostFix.convert('((q+x)*(y-z))/r')
        self.assertEqual(result, 'qx+yz-*r/',
                         "Cannot Multiply and Add Simultaneously")


class TestEvaluateMethod(unittest.TestCase):

    def test_basic_addition(self):
        result = PostFix.evaluate('1 2 +')
        self.assertEqual(result, 3.0, 'Cannot Add two Integers')

    def test_basic_subtraction(self):
        result = PostFix.evaluate('2 4 -')
        self.assertEqual(result, -2.0, "Cannot subtract two Integers")

    def test_basic_multiplication(self):
        result = PostFix.evaluate('3 4 *')
        self.assertEqual(result, 12.0, "Cannot Multiply two Integers")

    def test_basic_multiplication(self):
        result = PostFix.evaluate('4 2 /')
        self.assertEqual(result, 2.0, "Cannot Multiply two Integers")

    def test_division_and_subtraction(self):
        result = PostFix.evaluate('1 2 1 - /')
        self.assertEqual(result, 1.0,
                         "Cannot Divide and Subtract Simultaneously")

    def test_division_and_Multiplication(self):
        result = PostFix.evaluate('2 2 2 * /')
        self.assertEqual(result, 0.5,
                         "Cannot Divide and Multiply Simultaneously")

    def test_division_and_Addition(self):
        result = PostFix.evaluate('1 2 1 + /')
        self.assertEqual(result, float(1/3),
                         "Cannot Divide and Add Simultaneously")

    def test_Multiplication_and_Subtraction(self):
        result = PostFix.evaluate('1 - 2 6 - *')
        self.assertEqual(result, 4.0,
                         "Cannot Multiply and Subtract Simultaneously")

    def test_Multiplication_and_Addition(self):
        result = PostFix.evaluate('5 4 1 + *')
        self.assertEqual(result, 25.0,
                         "Cannot Multiply and Add Simultaneously")

    def test_Addition_and_Subtraction(self):
        result = PostFix.evaluate('1 - 4 3 - +')
        self.assertEqual(result, 0.0,
                         "Cannot Add and Subtract Simultaneously")

    def test_all_operators(self):
        result = PostFix.evaluate('1 2 + 4 3 - * 2 /')
        self.assertEqual(result, 1.5,
                         "Cannot Compute with all Operators Simultaneously")


if(__name__ == "__main__"):
    sys.path.append(os.path.abspath('../Algorithms'))
    from shuntingYard import PostFix
    unittest.main(exit=False)
