from zad6testy import runtests
from queue import PriorityQueue

def dijkstra(G,s,t):
    n = len(G)
    # distance for two states -> using normaln step, double step
    best_dist = [[float('inf') for _ in range(2)] for _ in range(n)]

    q = PriorityQueue()
    best_dist[s][0] = best_dist[s][1] = 0

    # (normaln_step, double_step, made_jump, dist_in_air, vertex)
    q.put((0,0,False,0,s))

    while q.empty() is False:
        normal_distance, double_distance,made_jumping, dist_in_air, current_location = q.get()

        for i in range(n):
            # process the child
            if G[current_location][i] != 0:

                # just made jump
                if made_jumping and best_dist[i][0] > double_distance + G[current_location][i]:
                    best_dist[i][0] = double_distance + G[current_location][i]
                    q.put((best_dist[i][0],best_dist[i][1], False,0,i))
                # process in the air case
                if dist_in_air != 0 and best_dist[i][1] > max(dist_in_air, G[current_location][i]) + normal_distance:
                    best_dist[i][1] = max(dist_in_air, G[current_location][i]) + normal_distance
                    q.put((best_dist[i][0],best_dist[i][1], False,0,i))
                # process two-case-avaible
                elif made_jumping is False:
                    if best_dist[i][0] > normal_distance + G[current_location][i]:
                        best_dist[i][0] = normal_distance + G[current_location][i]
                        q.put((best_dist[i][0],best_dist[i][1], False,0,i))
                    q.put((normal_distance,best_dist[i][1], True,G[current_location][i],i))

    return min(best_dist[t])


def jumper( G, s, w ):
    return dijkstra(G,s,w)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )