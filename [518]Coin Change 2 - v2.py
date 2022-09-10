class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0: return 1
        if len(coins) == 0: return 0

        M = len(coins)  # 0 coins, 1, 2, ...M
        N = amount
        # print(" m: ", M, " n: ", N)
        dp = [([1] + [0] * amount) for _ in range(M)]

        for ii in range(M):
            for jj in range(1, N + 1):
                if jj >= coins[ii]:
                    dp[ii][jj] = dp[ii - 1][jj] + dp[ii][jj - coins[ii]]
                else:
                    dp[ii][jj] = dp[ii - 1][jj]

        # print(dp)
        return dp[-1][-1]



