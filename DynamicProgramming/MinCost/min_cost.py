'''
    O,C - relax spots, relax costs
    T - max step
    L - the length of the root, that driver has to pass through

    Special condition: driver can make 2*T step, but only once in entire journey

    dp = 2-D array (first row for min result which does not use 2T step,
                    second row for min result which use 2T step or has already used it)

    f(i,0) = { min( f(i,0), f(j,0) + cost(j) ) }
    f(i,1) = { min( f(i,1), f(j,1) + cost(j), f(k,0) + cost(k) ) }
        where:
            i - current position
            j - positions with direct 1T step from j to i
            k - positions with direct 2T step from k to i

            f(0,0) = f(0,1) = 0

    Complexity: O(n^2)
'''


from kol2btesty import runtests
def min_cost( O, C, T, L ):

    n = len(O)
    n += 2
    Tab = [ None for _ in range(n)]
    Tab[0], Tab[-1] = (0,0), (L,0)
    k = 1
    for i in range(n-2):
        Tab[k] = (O[i], C[i])
        k+=1

    Tab.sort(key=lambda x:x[0])
    dp = [ [float('inf'), float('inf')] for _ in range(n) ]
    dp[0][0] = dp[0][1] = 0

    for i in range(1,n):
        for j in range(0,i+1):
            dist = Tab[i][0] - Tab[j][0]
            if dist <= T:
                dp[i][0] = min(dp[i][0], dp[j][0] + Tab[j][1])
                dp[i][1] = min(dp[i][1], dp[j][1] + Tab[j][1])
            elif dist <= 2*T:
                dp[i][1] = min(dp[i][1], dp[j][0] + Tab[j][1])

    return min(dp[-1])

runtests( min_cost, all_tests = True )
