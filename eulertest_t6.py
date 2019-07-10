from euler_t6 import sum_diff
import unittest

class Test(unittest.TestCase):

    def test_is_int(self):
        self.assertEqual(sum_diff(1.1), 'Number must be Integer!')

    def test_positive_number(self):
        self.assertEqual(sum_diff(-1), 'Number must be positive')

    def test_answer(self):
        self.assertEqual(sum_diff(10), 2640)


if __name__ == '__main__':
    unittest.main()