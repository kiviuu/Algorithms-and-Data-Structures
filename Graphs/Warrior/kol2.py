from kol2testy import runtests
from queue import PriorityQueue

def dijkstra(G, s, e):
  n = len(G)
  best_dist = [ [float('inf') for _ in range(17)] for _ in range(n) ]
  for i in range(17):
    best_dist[s][i] = 0
  q = PriorityQueue()
  # distance, state, vertex
  q.put((0, 0, s))


  while not q.empty():
    d, awake, u = q.get()
    if d > best_dist[u][awake]: continue
    if u == e: return d
    for child, distance in G[u]:
      #new distance for child
      new_dist = d + distance

      #new awake time for child
      new_awake_time = awake + distance

      if new_awake_time <= 16 and new_dist < best_dist[child][new_awake_time]:
        q.put((new_dist, new_awake_time, child))
        best_dist[child][new_awake_time] = new_dist

        if best_dist[child][0] > new_dist+8:
          q.put((new_dist+8,0, child))
          best_dist[child][0] = new_dist+8

  result = float('inf')
  finish_line = best_dist[e]
  for d in finish_line:
    result = min(result, d)
  return result


def warrior( G, s, t):
  # tu prosze wpisac wlasna implementacje
  graph = [[] for _ in range(max(max(u, v) for u, v, _ in G) + 1)]

  for edge in G:
    graph[edge[0]].append((edge[1], edge[2]))
    graph[edge[1]].append((edge[0], edge[2]))

  return dijkstra(graph, s, t)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )
