import random
import unittest

from p16 import *


def brute_force(n, k):
    "A hopelessly-slow but obviously-correct(?) implementation."
    k = str(k)
    return sum(str(i).count(k) for i in range(0, n + 1))


class TestBruteForce(unittest.TestCase):
    """Smoke tests for the brute-force algorithm.
    """
    def test_canned(self):
        self.assertEqual(
            brute_force(22, 2),
            6)

        self.assertEqual(
            brute_force(23, 2),
            7)


class Tests(unittest.TestCase):
    def test_canned(self):
        self.assertEqual(
            count(22, 2),
            6)

        self.assertEqual(
            count(23, 2),
            7)

    def test_against_brute_force(self):
        for i in range(10):
            val = random.randint(0, 100000)
            self.assertEqual(
                brute_force(val, 2),
                count(val, 2))


class TestSlow(unittest.TestCase):
    def test_canned(self):
        self.assertEqual(
            slow_count(22, 2),
            6)

        self.assertEqual(
            slow_count(23, 2),
            7)

    def test_against_brute_force(self):
        for i in range(10):
            val = random.randint(0, 100000)
            self.assertEqual(
                brute_force(val, 2),
                slow_count(val, 2))


if __name__ == '__main__':
    unittest.main()
