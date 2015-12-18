import unittest

from p10 import *


class TestBefore(unittest.TestCase):
    pass


class TestAfter(unittest.TestCase):
    pass


class TestSolution(unittest.TestCase):
    def test_solution(self):
        prices = list(read_data("p10_input.txt"))
        self.assertEqual(
            best_profit(prices),
            89.5850)
