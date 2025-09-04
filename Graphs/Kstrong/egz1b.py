"""
Try to extend previous (for i-1) max sum using next element T[j]:
  We are going through nest row in dp table so we have option to skip one more element,
  that's why in comparison it is necessary to compare two cases:
    1) include new element into this sum (take dp[i][j-1] // prev max sum for this row // + T[i]
    2) do not include into sum (take dp[i-1][j-1])

  init:
    dp[0][i] = max(dp[0][i-1] + T[i], T[i]) for i in <0, n-1>
  step:
    dp[i][j] = max(dp[i][j-1] + T[j], dp[i-1][j-1]) for i in <1, k> and j in <i, n-1>

  Time complexity: O(nk)
  n - T.length
  k - exclude limit
"""

from egz1btesty import runtests
def kstrong( T, k):
  n = len(T)
  dp = [ [ float("-inf") for _ in range(n) ] for _ in range(k+1) ]

  # init
  dp[0][0] = T[0]
  for i in range(1, n):
    dp[0][i] = max(T[i], dp[0][i-1] + T[i])

  for i in range(1, k+1):
    for j in range(i, n):
      dp[i][j] = max(dp[i-1][j-1], dp[i][j-1]+T[j])

  result = max(dp[-1])
  for i in range(k+1):
    result = max(result, dp[i][-1])

  return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )
