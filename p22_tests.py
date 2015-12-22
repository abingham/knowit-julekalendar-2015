import unittest

from p22 import *


class Tests(unittest.TestCase):
    def test_canned(self):
        self.assertEqual(convert("abc"), 2)
        self.assertEqual(convert("qywo"), 4)

    def test_solution(self):
        self.assertEqual(
            convert('evdhtiqgfyvcytohqppcmdbultbnzevdbakvkcdpbatbtjlmzaolfqfqjifkoanqcznmbqbeswglgrzfroswgxoritbw'),
            453)

if __name__ == "__main__":
    unittest.main()
