"""
Solution:
    C[i] - list of prices for one amount of fuel on 'i' planet
    T[i] - list of tuples where elements are (j,c); where 'j' is destination planet and 'c' is cos to travel
    D[i] - list of distances ( from planet with index 0 )
    dp -> n*E ( where n = amount of planets and E = state of tank )
    dp[i][j] -> minimum cost to travel to this planet from planet 0 with 'j' amount of fuel ( can be filled )

    Steps:
        1) init
            1.1) dp[0][j] = C[0]*j;   where 'j' in <0, E>
            1.2) tp_on - list of lists where every tp_on[i] element ( that element is type of list )
                 contain tuples (j,c); where 'i' is destination plant, 'j' is start planet and 'c' is cost to use this
                 teleport

        2) fill row 'i', where 'i' in <1, n>
            2.1) base available travel ( without refill )
            k - distance from planet 'i-1' to 'i'
            idx - special index ( necessary to fill dp table from 0 index )
            dp[i][idx] = dp[i-1][j];    where 'j 'in <k, E+1>
            2.2) check available teleports which can be used to travel to 'i' planet
            and if this option is better than use it
            2.3) validate row / fill row to the end using this rules:
                if it is better to fill the tank on this ('i') planet then do it
                dp[i][j] = min( dp[i][j], dp[i][j-1]+C[i];  where 'j' in <1, E+1>
"""


from egz1btesty import runtests

def planets( D, C, T, E ):
    n = len(D)
    tp_on = [ [] for _ in range(n) ]
    for i in range(n):
        dst, cst = T[i]
        if i != dst:
            tp_on[dst].append((i, cst))

    dp = [ [ float("inf") for _ in range(E+1) ] for _ in range(n) ]

    # init
    for i in range(E+1):
        dp[0][i] = C[0]*i

    for i in range(1, n):
        k = D[i] - D[i-1]
        idx = 0
        # base available travel
        for j in range(k, E+1):
            dp[i][idx] = dp[i-1][j]
            idx += 1

        # can teleport from previous plant and is it better than current cost?
        if len(tp_on[i]) > 0:
            for from_idx, cost in tp_on[i]:
                if dp[from_idx][0] + cost < dp[i][0]:
                    dp[i][0] = dp[from_idx][0] + cost

        # validate row
        for j in range(1, E+1):
            if dp[i][j-1] + C[i] < dp[i][j]:
                dp[i][j] = dp[i][j-1] + C[i]

    return dp[-1][0]

runtests( planets, all_tests = True )
