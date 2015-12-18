import unittest

from p10 import *


class TestBefore(unittest.TestCase):
    def test_basic(self):
        prices = [12, 10, 23, 19, 18]
        before = calc_before(prices)
        self.assertListEqual(
            before,
            [-2, -2, 13, 13, 13])


class TestAfter(unittest.TestCase):
    pass


class TestSolution(unittest.TestCase):
    def test_solution(self):
        prices = list(read_data("p10_input.txt"))
        self.assertEqual(
            best_profit(prices),
            89.5850)

if __name__ == '__main__':
    unittest.main()
