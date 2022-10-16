def solve_knapsack(profits, weights, capacity):
  N=len(profits)
  dp=[0 for _ in range(capacity+1)]

  # when only item 1
  for ii in range(capacity+1):
    if ii >= weights[0]:
      dp[ii]=profits[0]

  for ii in range(1, N):
    for jj in reversed(range(capacity+1)):
      dp[jj]=max(dp[jj], (dp[jj-weights[ii]]+profits[ii]) if weights[ii]<=jj else 0)

  return dp[-1]


def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
