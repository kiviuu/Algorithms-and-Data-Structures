from kolutesty import runtests

def dfs(G):
  n = len(G)
  visited = [False] * n
  parent = [None] * n
  time = 0
  result = []
  def dfs_visit(G,v):
    nonlocal time, visited, parent, result
    visited[v] = True
    time += 1
    for u in G[v]:
      if visited[u] is False:
        parent[u] = v
        dfs_visit(G,u)
    time += 1
    result.append(v)

  for v in range(n):
    if visited[v] is False:
      dfs_visit(G,v)

  return result[::-1]


def projects(n, L):
  G = [ [] for _ in range(n) ]
  tracker = [ 0 for _ in range(n) ]
  for edge in L:
    G[edge[1]].append(edge[0])

  top_sorted = dfs(G)
  for v in top_sorted:
    tracker[v] += 1
    for u in G[v]:
      tracker[u] = max(tracker[u], tracker[v])

  return max(tracker)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( projects, all_tests = True )
