from functools import lru_cache
def solve_knapsack(profits, weights, capacity):
  # TODO: Write your code here

  N=len(profits)

  @lru_cache(None)
  def dp(st, cost):
    if st >= N:
      return 0

    tke=0
    if cost >= weights[st]:
      tke=profits[st] + dp(st+1, cost-weights[st])
    ntk = dp(st+1, cost)
    return max(tke, ntk)


  return dp(0, capacity)


def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
