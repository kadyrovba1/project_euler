from euler_t10 import sum_primes
import unittest


class Test(unittest.TestCase):
    def test_negative_number(self):
        self.assertEqual(sum_primes(-3), 'Number must be positive')

    def test_not_integer(self):
        self.assertEqual(sum_primes('5'), 'Input must be Integer')

    def test_result(self):
        self.assertEqual(sum_primes(10), 17)


if __name__ == '__main__':
    unittest.main()