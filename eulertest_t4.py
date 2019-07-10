from euler_t4 import n
import unittest


class Test(unittest.TestCase):
    def test_result(self):
        self.assertEqual(n, 906609)


if __name__ == '__main__':
    unittest.main()