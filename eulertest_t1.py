from euler_t1 import sum_of_multiples
import unittest

class Test(unittest.TestCase):
    def test_negative_number(self):
        self.assertEqual(sum_of_multiples(-3), 'Number must be positive')

    def test_not_integer(self):
        self.assertEqual(sum_of_multiples('5'), 'Input must be Integer')

    def test_result(self):
        self.assertEqual(sum_of_multiples(10), 23)


if __name__ == '__main__':
    unittest.main()