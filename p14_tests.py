import unittest

from p14 import *


def _is_mirrored(s):
    for i in range(len(s) // 2):
        front = s[i]
        back = s[(i + 1) * -1]
        if REFLECTIONS[front] != back:
            return False
    return True


class TestMirrorables(unittest.TestCase):
    def test_length_1(self):
        self.assertEqual(
            list(sorted(map(int, mirrorables(1)))),
            [0, 1, 6, 8, 9])

    def test_length_2(self):
        self.assertEqual(
            list(sorted(map(int, mirrorables(2)))),
            [0, 1, 6, 8, 9,
             10, 11, 16, 18, 19,
             60, 61, 66, 68, 69,
             80, 81, 86, 88, 89,
             90, 91, 96, 98, 99]
        )


class TestMirrored(unittest.TestCase):
    def test_lots(self):
        for i in itertools.islice(mirrored(), 10000):
            self.assertTrue(_is_mirrored(i))

    def test_101(self):
        self.assertIn(
            '101',
            list(itertools.islice(mirrored(), 1000)))


class TestShort(unittest.TestCase):
    def test_short(self):
        # Since mirrored_short() only returns values up to 100000, don't make
        # the comparison size too large.
        self.assertEqual(
            sorted(map(int, itertools.islice(mirrored(), 50))),
            sorted(map(int, itertools.islice(mirrored_short(), 50))))


class TestSolution(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(), 99)


if __name__ == '__main__':
    unittest.main()
    # print(list(itertools.islice(mirrored(), 10)))
