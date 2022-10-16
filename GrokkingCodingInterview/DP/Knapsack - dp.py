def solve_knapsack(profits, weights, capacity):
  """
  : dp[ii][jj]: the max profit achievable where
                ii the index of the items.
                jj the ttl cost allowed

  """
  N=len(profits)
  dp=[[-1 for _ in range(capacity+1)] for _ in range(N)]

  # when c=0
  for ii in range(N):
    dp[ii][0]=0

  for ii in range(1, capacity+1):
    dp[0][ii] = profits[0] if ii >= weights[0] else 0

  for ii in range(1, N):
    for jj in range(1, capacity+1):
      dp[ii][jj]= max(dp[ii-1][jj], dp[ii-1][jj-weights[ii]]+profits[ii] if weights[ii]<=jj else 0)

  return dp[-1][-1]


def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
