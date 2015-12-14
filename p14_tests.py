import unittest

from p14 import *


def _is_mirrored(a):
    s = str(a)
    for i in range(len(s) // 2):
        front = int(s[i])
        back = int(s[(i + 1) * -1])
        if REFLECTIONS[front] != back:
            return False
    return True


class TestsToInt(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(to_int(()), 0)

    def test_simple(self):
        self .assertEqual(to_int((1, 2, 3)), 123)
        self.assertEqual(to_int((4, 5, 6)), 456)

    def test_leading_zero(self):
        self.assertEqual(to_int((0, 1, 2, 3)), 123)


class TestMirrorables(unittest.TestCase):
    def test_length_2(self):
        self.assertEqual(
            list(sorted(map(to_int, mirrorables(2)))),
            [11, 16, 18, 19, 61, 66, 68, 69, 81, 86, 88, 89, 91, 96, 98, 99]
        )


class TestMirrored(unittest.TestCase):
    def test_lots(self):
        for i in itertools.islice(mirrored(), 10000):
            self.assertTrue(_is_mirrored(i))

if __name__ == '__main__':
    unittest.main()
    # print(list(itertools.islice(mirrored(), 10)))
