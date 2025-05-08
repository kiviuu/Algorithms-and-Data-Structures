from zad4testy import runtests
from queue import PriorityQueue

def dijkstra(G, s):
    n= len(G)
    dist = [ float('inf') for _ in range(n) ]
    parent = [ None for _ in range(n) ]
    q = PriorityQueue()
    dist[s] = 0
    q.put((0, s))

    def relax(u,v,w):
        nonlocal dist, parent
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            parent[v] = u
            return True
        return False

    while not q.empty():
        p,u = q.get()
        if p != dist[u]: continue
        for v, w in G[u]:
            if relax(u,v,w):
                q.put((dist[v],v))
    return dist

def spacetravel( n, E, S, a, b ):
    # create graph adj list
    G = [ [] for _ in range(n) ]
    for start, end, cost in E:
        G[start].append((end,cost))
        G[end].append((start,cost))

    # connect black holes into cycle
    for i in range(len(S)-1):
        G[S[i]].append((S[i+1],0))
        #G[S[i+1]].append((S[i],0))
    G[S[-1]].append((S[0],0))


    #find the shortest paths
    if dijkstra(G,a)[b] == float('inf'):
        return None
    return dijkstra(G,a)[b]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
