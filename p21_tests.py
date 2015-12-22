import unittest

from p21 import *


class Tests(unittest.TestCase):
    """"
    start = "pull", slutt = "pool", ordliste = ["peel", "poll", "ping", "push", "pool"]
    Her er den korteste transformasjonssekvensen "pull" -> "poll" -> "pool", og denne sekvensen har lengde 3
    """

    def test_canned(self):
        g = build_graph(["pull", "peel", "poll", "ping", "push", "pool"])
        cost, path = dijkstra(g, "pull", "pool")
        self.assertListEqual(list(path), ["pull", "poll", "pool"])
        self.assertEqual(len(path), 3)

if __name__ == '__main__':
    unittest.main()
