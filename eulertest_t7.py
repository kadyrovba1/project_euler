from euler_t7 import prime
import unittest


class Test(unittest.TestCase):
    def test_negative_number(self):
        self.assertEqual(prime(-3), 'Number must be positive')

    def test_not_integer(self):
        self.assertEqual(prime('5'), 'Input must be Integer')

    def test_result(self):
        self.assertEqual(prime(6), 13)


if __name__ == '__main__':
    unittest.main()