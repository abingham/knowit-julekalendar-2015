"""
Gitt to ord (start og slutt) og en ordliste (list). Finn lengden av den korteste transformasjonssekvensen fra startordet til sluttordet.
Følgende regler gjelder for hver transformasjon:
* Kun en bokstav kan endres om gangen
* Hvert mellomord må finnes i ordlisten

For eksempel:
start = "pull", slutt = "pool", ordliste = ["peel", "poll", "ping", "push", "pool"]
Her er den korteste transformasjonssekvensen "pull" -> "poll" -> "pool", og denne sekvensen har lengde 3

Hva er sekvenslengden for startordet “sand”,  sluttordet “hold” og ordlisten som finnes på http://pastebin.com/LJX9cNvA?
"""

from collections import defaultdict
from heapq import heappop, heappush
from itertools import chain


# copied from http://hetland.org/coding/python/levenshtein.py
def levenshtein(a, b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a, b = b, a
        n, m = m, n

    current = range(n+1)
    for i in range(1, m + 1):
        previous, current = current, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete = previous[j] + 1, current[j - 1] + 1
            change = previous[j - 1]
            if a[j - 1] != b[i - 1]:
                change = change + 1
            current[j] = min(add, delete, change)

    return current[n]


def dijkstra(g, f, t):
    q = [(0, f, ())]
    seen = set()

    while q:
        cost, v1, path = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1,) + path
            if v1 == t:
                return (cost, tuple(reversed(path)))

            for v2, c in g.get(v1, {}).items():
                if v2 not in seen:
                    heappush(q, (cost + c, v2, path))

    return float("inf")


def read_data(filename):
    with open(filename, 'r') as f:
        yield from filter(bool, map(str.strip, f))


def build_graph(data):
    g = defaultdict(dict)
    for i1, v1 in enumerate(data):
        for v2 in data[i1 + 1:]:
            dist = levenshtein(v1, v2)
            if dist == 1:
                g[v1][v2] = dist
                g[v2][v1] = dist
    return g


if __name__ == '__main__':
    data = list(chain(("sand",), read_data("p21_words.txt")))
    g = build_graph(data)
    cost, path = dijkstra(g, "sand", "hold")
    print(len(path))

