from euler_t8 import largest_product
import unittest

class Test(unittest.TestCase):

    def test_is_int(self):
        self.assertEqual(largest_product(1.1), 'Number must be Integer!')

    def test_positive_number(self):
        self.assertEqual(largest_product(-1), 'Number must be greater 1')

    def test_answer(self):
        self.assertTrue(largest_product(4), 5832)


if __name__ == '__main__':
    unittest.main()