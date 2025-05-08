from egz3atesty import runtests
from collections import deque

def bfs(G, s, n, crt_state, nr_parasite):
  visited = [ False for _ in range(n) ]
  parent = [ None for _ in range(n) ]
  dist = [ float('inf') for _ in range(n) ]
  q = deque()
  q.append(s)
  visited[s] = True
  dist[s] = 0
  crt_state[s] = (nr_parasite, 0, None)
  while q:
    u = q.popleft()
    for v in G[u]:
      if visited[v] is False:
        visited[v] = True
        parent[v] = u
        dist[v] = dist[u] + 1
        q.append(v)
        if crt_state[v][1] >= dist[u]+1:
          crt_state[v] = (nr_parasite, dist[u] + 1, u)
  return dist, parent


def mykoryza( G,T,d ):
  # tu prosze wpisac wlasna implementacje

  # (nr_grzyba, czas_odwiedzenia, rodzic)
  current_state = [ (float('inf'),float('inf'),None) for _ in range(len(G)) ]

  k = len(T)
  for i in range(k-1,-1,-1):
    bfs(G,T[i],len(G), current_state, i)

  result = 0
  for v in range(len(G)):
    if current_state[v][0] == d:
      result += 1

  return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( mykoryza, all_tests = True )
