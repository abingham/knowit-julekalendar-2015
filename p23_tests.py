import unittest

from p23 import cut_count, INPUT


class Tests(unittest.TestCase):
    def test_canned(self):
        self.assertListEqual(
            cut_count([5, 4, 4, 2, 2, 8]),
            [6, 4, 2, 1])

    def test_solution(self):
        self.assertListEqual(
            cut_count(INPUT),
            [])

if __name__ == '__main__':
    unittest.main()
