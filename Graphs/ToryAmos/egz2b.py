from egz2btesty import runtests
from queue import PriorityQueue


def dijkstra(G, s):
    n = len(G)
    # dist[station][0]: min cost to reach station arriving via 'I' gauge
    # dist[station][1]: min cost to reach station arriving via 'P' gauge
    # This state expansion is necessary because future costs depend on the arrival gauge.
    dist = [[float("inf"), float("inf")] for _ in range(n)]

    # Parent array for path reconstruction (unused in this problem, but kept for completeness).
    parent = [None for _ in range(n)]

    # Priority queue to select the next station with smallest cost.
    # Stores (cost, station, incoming_gauge), where incoming_gauge is 'I', 'P', or None (for start).
    q = PriorityQueue()

    # Initialize starting station with cost 0 for both gauges (though we use None for flexibility).
    # This allows uniform handling in relaxation.
    dist[s][0], dist[s][1] = 0, 0

    # Enqueue start with None as incoming_gauge to indicate no prior station cost.
    q.put((0, s, None))

    # Main Dijkstra loop: process until queue is empty.
    while q.empty() is False:
        # Extract the minimum cost entry.
        p, u, t_in = q.get()

        # Determine the gauge index for the current station based on t_in.
        # If t_in is None (start), arbitrarily use index 1 (since dist[s][0] == dist[s][1] == 0).
        u_idx = 0 if t_in == 'I' else 1

        # Skip if this is an outdated entry (better path already found).
        if p != dist[u][u_idx]: continue

        # For each neighbor v connected from u.
        for v, w, t_out in G[u]:
            # Determine the target gauge index based on outgoing gauge.
            v_idx = 0 if t_out == 'I' else 1

            # Base travel cost is the edge distance w.
            true_dist = w

            # Add station processing cost at u (before leaving to v).
            # If t_in == t_out (same gauge, no change).
            if t_in == t_out:
                if t_in == 'I':
                    true_dist += 5  # Cost for 'I' same-gauge pass.
                elif t_in == 'P':
                    true_dist += 10  # Cost for 'P' same-gauge pass.
            # If gauges differ and not starting point.
            elif t_in is not None:
                true_dist += 20  # Gauge change cost.
            # If t_in is None (starting at u=s), no station cost added.

            # Relaxation: check if this path improves the cost to v arriving via t_out.
            if dist[v][v_idx] > dist[u][u_idx] + true_dist:
                # Update the distance.
                dist[v][v_idx] = dist[u][u_idx] + true_dist

                # Update parent (unused, but for completeness).
                parent[v] = u

                # Enqueue the updated neighbor with t_out as its incoming_gauge for next steps.
                q.put((dist[v][v_idx], v, t_out))

    # Return the 2D dist array for all stations.
    return dist


def tory_amos(E, A, B):
    # Determine the number of stations by finding the max station ID + 1.
    n = 0
    for v, u, w, t in E:
        n = max(n, v, u)
    n += 1

    # Build adjacency list: G1[station] = list of (neighbor, distance, gauge_type).
    # Add both directions since edges are bidirectional.
    G1 = [[] for _ in range(n)]
    for v, u, w, t in E:
        G1[v].append((u, w, t))
        G1[u].append((v, w, t))

    # Run Dijkstra from A.
    result = dijkstra(G1, A)

    # Return the minimum cost to B, considering arrival via either gauge.
    # If unreachable, would be inf, but assuming connected in tests.
    return min(result[B])


# Run tests (set all_tests = True to run all).
runtests(tory_amos, all_tests=True)