from euler_t3 import largest_prime
import unittest


class Test(unittest.TestCase):
    def test_negative_number(self):
        self.assertEqual(largest_prime(-3), 'Number must be positive')

    def test_not_integer(self):
        self.assertEqual(largest_prime('5'), 'Input must be Integer')

    def test_result(self):
        self.assertEqual(largest_prime(13195), 29)


if __name__ == '__main__':
    unittest.main()