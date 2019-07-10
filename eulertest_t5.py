from euler_t5 import smallest
import unittest


class Test(unittest.TestCase):
    def test_result(self):
        self.assertEqual(smallest(), 232792560)


if __name__ == '__main__':
    unittest.main()