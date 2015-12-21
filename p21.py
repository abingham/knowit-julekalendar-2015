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

# copied from http://hetland.org/coding/python/levenshtein.py
def levenshtein(a,b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n
        
    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)
            
    return current[n]


# Originally by David Eppstein
# http://code.activestate.com/recipes/119466-dijkstras-algorithm-for-shortest-paths/
def dijkstra(G,start,end=None):
    D = {}  # dictionary of final distances
    P = {}  # dictionary of predecessors
    Q = priorityDictionary()   # est.dist. of non-final vert.
    Q[start] = 0

    for v in Q:
        D[v] = Q[v]
        if v == end:
            break

        for w in G[v]:
            vwLength = D[v] + G[v][w]
            if w in D:
                if vwLength < D[w]:
                    raise ValueError(
                        "Dijkstra: found better path to already-final vertex")
                elif w not in Q or vwLength < Q[w]:
                    Q[w] = vwLength
                    P[w] = v

    return (D, P)


def read_data(filename):
    with open(filename, 'r') as f:
        yield from filter(bool, map(str.strip, f))


def build_graph(data):
    g = {}
    for v1 in data:
        v1_subgraph = {}
        for v2, v2_subgraph in g.items():
            dist = levenshtein(v1, v2)
            v2_subgraph[v1] = dist
            v1_subgraph[v2] = dist
        g[v1] = v1_subgraph
    return g

