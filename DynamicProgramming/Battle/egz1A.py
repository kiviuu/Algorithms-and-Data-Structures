"""
Solution:
    1) create table for entire battlefield ( from task description we know the last possible index is 4n+4m-1 )
    2) locate catapults and processors on battlefield in tuple
    3) go from 0 through entire battlefield
        3.1) when field is empty -> skip this field
        3.2) when there is catapult on the field -> put it`s max reachable index in the stack
        3.3) when processor is on the field -> get catapult from the stack and try to shot this processors
Why it works?
    The key points to notice is, the most efficient connection between catapult and processor is:
        this processor connected to the closest catapult on it`s left (greedy part)
Time complexity:
    O(n+m)  - greedy algorithm
"""

from egz1Atesty import runtests
from collections import deque

def battle(P,K,R):
    n = len(P)
    m = len(K)
    k = 4*n + 4*m

    # battlefield
    arrow = [ None for _ in range(k) ]

    # locate objects
    # (obj_type, max_reachable_index)
    for pos in P:
        arrow[pos] = ("P", float("-inf"))
    for i in range(m):
        pos, r = K[i], R[i]
        arrow[pos] = ("K", pos+r)

    # stack for catapults
    q = deque()

    result = 0
    for i in range(k):
        if arrow[i] is None:
            continue

        obj_type, max_range = arrow[i]

        if obj_type == "K":
            q.append(max_range)
            continue

        if obj_type == "P":
            while q:
                max_reachable_index = q.pop()
                if max_reachable_index >= i:
                    result += 1
                    break
    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( battle, all_tests=True )