import unittest

from p16 import *


class Tests(unittest.TestCase):
    def test_canned(self):
        self.assertEqual(
            two_count(22),
            6)

        self.assertEqual(
            two_count(23),
            7)



if __name__ == '__main__':
    unittest.main()
