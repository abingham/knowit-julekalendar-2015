import unittest

from p15 import *


class Tests(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(
            list(solve(MAP, 11)),
            [11, 34, 42, 15, 25, 31, 54, 13, 32, 45,
             35, 23, 43, 51, 21, 14, 41, 33, 52])

if __name__ == '__main__':
    unittest.main()
