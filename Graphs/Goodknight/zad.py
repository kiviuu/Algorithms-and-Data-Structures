from zadtesty import runtests
from queue import PriorityQueue

def dijkstra(G, s, e):

  # best dist in weakness state tracking table
  best_dist = [ [ float('inf') for _ in range(17) ] for _ in range(len(G)) ]
  for i in range(17):
    best_dist[0][i] = 0
  q = PriorityQueue()

  # a queue element contains: ( current_distance, current_weakness, vertex )
  q.put((0,0,s))

  while not q.empty():
    dist, awake_time, u = q.get()

    # direct connection s to e
    if u == e: return dist

    # distance edge is grater than current best minimum distance
    if dist > best_dist[u][awake_time]: continue

    # looking for the u-vertex neighbors
    for i in range(len(G)):

      # process neighbor
      if G[u][i] != -1:

        # distance to the neighbor vertex in process
        new_dist = dist + G[u][i]

        # new level of weakness for the neighbor, after travel through the edge
        child_awake_time = awake_time + G[u][i]

        # if warrior is able to travel through edge with his current level of weakness and
        # his new distance through this edge is better than distance stored in tracking table
        if child_awake_time <= 16 and new_dist < best_dist[i][child_awake_time]:

          # update new best distance to this vertex
          best_dist[i][child_awake_time] = new_dist
          # and put it in the queue
          q.put((new_dist, child_awake_time, i))

          # if the stored min distance for rested warrior in visited vertex is grater than
          # new calculated distance increased by 8 (resting)
          if best_dist[i][0] > new_dist+8:
            # add case for resting warrior
            q.put((new_dist+8, 0, i))


  # looking for the best minimum time in the finish line
  result = float('inf')
  finish_line = best_dist[e]
  for time in finish_line:
    result = min(result, time)
  return result


def goodknight( G, s, t ):
  # tu prosze wpisac wlasna implementacje
  return dijkstra(G, s, t)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )
