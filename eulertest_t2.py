from euler_t2 import fib
import unittest


class Test(unittest.TestCase):
    def test_negative_number(self):
        self.assertEqual(fib(-3), 'Number must be positive')

    def test_not_integer(self):
        self.assertEqual(fib('5'), 'Input must be Integer')

    def test_result(self):
        self.assertEqual(fib(10), 10)


if __name__ == '__main__':
    unittest.main()