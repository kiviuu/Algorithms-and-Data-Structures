from egz1atesty import runtests

# 1. use dijkstra to find min path to bikes
# 2. use dijkstra from finishline to bikes
# 3. find the best optional bike

from queue import PriorityQueue
def dijkstra(G,s):
  Q = PriorityQueue()
  n = len(G)
  dist = [float("inf")] * n
  parent = [None] * n
  dist[s] = 0
  Q.put((0,s))
  def relax(u,v,w):
    nonlocal parent, dist
    if dist[v] > dist[u]+w:
      dist[v] = dist[u]+w
      parent[v] = u
      Q.put((dist[v],v))

  while Q.empty() is False:
    d, u = Q.get()
    if d != dist[u]: continue
    for v, w in G[u]:
      relax(u,v,w)
  return dist



def armstrong( B, G, s, t):
  # tu prosze wpisac wlasna implementacje
  # create adj list
  n = 0
  for edge in G:
    n = max(n, edge[0], edge[1])
  graph = [ [] for _ in range(n+1) ]
  for edge in G:
    graph[edge[0]].append((edge[1], edge[2]))
    graph[edge[1]].append((edge[0], edge[2]))

  from_s = dijkstra(graph,s)
  from_t = dijkstra(graph,t)

  finish = from_s[t]

  for b_v, p, q in B:
    true_distance = from_s[b_v] + from_t[b_v] * (p/q)
    finish = min(finish, true_distance)

  if finish == float('inf'): return -1
  return int(finish)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )
