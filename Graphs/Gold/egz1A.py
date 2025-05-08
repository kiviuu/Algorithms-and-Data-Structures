from egz1Atesty import runtests
from queue import PriorityQueue

def dijkstra(G,s,is_wanted,r):
  n = len(G)
  parent = [None] * n
  cost = [float('inf')] * n
  q = PriorityQueue()
  cost[s] = 0
  q.put((0,s))

  def relax(u,v,w):
    nonlocal parent, cost
    if is_wanted:
      w = (2*w)+r
    if cost[v] > cost[u] + w:
      cost[v] = cost[u] + w
      parent[v] = u
      q.put((cost[v],v))


  while q.empty() is False:
    current_cost, u = q.get()
    if current_cost > cost[u]: continue
    for v,w in G[u]:
      relax(u,v,w)
  return cost


def gold(G,V,s,t,r):
  cost_to_castle = dijkstra(G,s,False,0)

  min_cost = cost_to_castle[t]

  #  V^3logV
  #for i in range(len(V)):
  #  cost_to_end = dijkstra(G,i,True,r)
  #  cal_cost = cost_to_castle[i] + cost_to_end[t] - V[i]
  #  min_cost = min(min_cost,cal_cost)


  #  V^2logV :D
  cost_from_end = dijkstra(G,t,True,r)

  for i in range(len(V)):
    true_cost = cost_to_castle[i] + cost_from_end[i] - V[i]
    min_cost = min(min_cost,true_cost)

  return min_cost

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
