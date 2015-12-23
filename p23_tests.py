import unittest

from p23 import cut_count, INPUT


class Tests(unittest.TestCase):
    def test_canned(self):
        self.assertListEqual(
            list(cut_count([5, 4, 4, 2, 2, 8])),
            [6, 4, 2, 1])

    def test_solution(self):
        self.assertListEqual(
            list(cut_count(INPUT)),
            [94,93,92,91,90,89,88,87,85,83,82,78,77,76,75,71,70,69,68,67,65,63,61,60,59,58,56,55,54,53,52,51,49,48,47,45,43,42,40,39,38,35,34,32,31,28,27,25,23,22,20,19,18,17,16,15,14,13,11,9,6,2])

if __name__ == '__main__':
    unittest.main()
