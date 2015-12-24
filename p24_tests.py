import unittest

from p24 import sum_through


def brute(i):
    return sum(range(1, (int(i) + 1)))


class Tests(unittest.TestCase):
    def test_canned(self):
        self.assertEqual(
            sum_through(10),
            55)

    def test_compare_to_brute(self):
        for i in (10, 1024, 10004):
            self.assertEqual(
                sum_through(i),
                brute(i))

if __name__ == '__main__':
    unittest.main()
