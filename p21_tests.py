import unittest

from p21 import *


class Tests(unittest.TestCase):
    """"
    start = "pull", slutt = "pool", ordliste = ["peel", "poll", "ping", "push", "pool"]
    Her er den korteste transformasjonssekvensen "pull" -> "poll" -> "pool", og denne sekvensen har lengde 3
    """

    def test_canned(self):
        g = build_graph(["peel", "poll", "ping", "push", "pool"])
        d = dijkstra(g, "pull")
        print(d)

if __name__ == '__main__':
    unittest.main()
