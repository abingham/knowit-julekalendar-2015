import unittest

from p18 import *


class Tests(unittest.TestCase):
    def test_canned_1(self):
        self.assertEqual(
            solve([3, 30, 34, 5, 9]),
            9534330)

    def test_canned_2(self):
        self.assertEqual(
            solve([128, 12]),
            12812)

    def test_canned_3(self):
        self.assertEqual(
            solve([824, 938, 1399, 5607, 6973, 5703, 9609, 4398, 8247]),
            9609938824824769735703560743981399)


if __name__ == '__main__':
    unittest.main()
