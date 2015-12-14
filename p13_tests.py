from itertools import islice
import unittest

from p13 import *


class Tests(unittest.TestCase):
    def test_canned(self):
        self.assertEqual(
            list(islice(knalltallene(), 10)),
            [1, 2, 3, 4, 5, 6, 8, 9, 10, 12])

if __name__ == '__main__':
    unittest.main()
