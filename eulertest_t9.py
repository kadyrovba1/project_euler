from euler_t9 import triplet
import unittest

class Test(unittest.TestCase):

    def test_answer(self):
        self.assertEqual(triplet(), '5 12 13')


if __name__ == '__main__':
    unittest.main()