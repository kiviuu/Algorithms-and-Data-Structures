"""
Solution:
    Modify graph: dijkstra can go into every resort vertex but can not go out and
    that change allow us to prevent every next trip through already visited resort vertex

    Time complexity:
        2R + 2E + ElogV -> O(ElogV)
        R - resorts.length
        E - flights.length
        V - amount of cities
"""

from kol2testy import runtests
from queue import PriorityQueue

def dijkstra(s, G):
    n = len(G)
    dist = [ float("inf") for _ in range(n) ]
    parent = [ None for _ in range(n) ]
    q = PriorityQueue()
    dist[s] = 0
    q.put((0, s))


    def relax(v,u,w):
        nonlocal parent, q, G, dist
        if dist[u] > dist[v] + w:
            dist[u] = dist[v] + w
            parent[u] = v
            q.put((dist[u], u))


    while q.empty() is False:
        p, v = q.get()
        if p != dist[v]: continue
        for u, w in G[v]:
            relax(v, u, w)
    return dist


def lets_roll(start_city, flights, resorts):
    n = 0
    for v, u, w in flights:
        n = max(n, v, u)
    n += 1

    G = [ [] for _ in range(n) ]

    for v, u, w in flights:
        G[v].append((u, w))
        G[u].append((v, w))

    for resort in resorts:
        G[resort] = []

    dist = dijkstra(start_city, G)

    result = 0

    for resort in resorts:
        if dist[resort] != float("inf"):
            result += ( dist[resort] * 2 )

    return result

runtests(lets_roll, all_tests = True)
