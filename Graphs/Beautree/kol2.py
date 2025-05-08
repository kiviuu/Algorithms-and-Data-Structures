from kol2testy import runtests
from collections import deque

def bfs(E, n, p, q):
    G = [[] for _ in range(n)]
    min_sum = 0
    for i in range(p,q+1):
        u,v,w = E[i]
        G[u].append(v)
        G[v].append(u)
        min_sum += w
    visited = [False] * n
    parent = [None] * n

    q = deque()
    visited[0] = True
    q.append(0)

    while q:
        u = q.popleft()
        for v in G[u]:
            if visited[v] is False:
                visited[v] = True
                parent[v] = u
                q.append(v)
            elif v != parent[u]:
                return -1
    if visited.count(True) == n:
        return min_sum
    return -1


def beautree(G):
    used_edge = [[False for _ in range(len(G))] for _ in range(len(G))]
    E = []
    for i in range(len(G)):
        for j in range(len(G[i])):
            u, w = G[i][j]
            if used_edge[u][i] is False:
                E.append((u,i,w))
                used_edge[u][i] = True
                used_edge[i][u] = True
    E.sort(key=lambda x: x[2])
    p=0
    q = len(G)-2
    while q<=len(E)-1:
        result = bfs(E,len(G),p,q)
        if result != -1: return result
        p+=1
        q+=1
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )
