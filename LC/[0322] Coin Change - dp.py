class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        : optimized counting => DP
        : dp[ii][jj]: least num of coins using upto ii coins make up amt=jj
        : least->Greedy
        """
        N=amount
        M=len(coins)

        dp=[[float('inf')]*(N+1) for _ in range(M)]

        # amt=0
        for ii in range(M):
            dp[ii][0]=0

        # using only the 1st coin
        for jj in range(1, N+1):
            if jj%coins[0]==0:
                dp[0][jj]=jj//coins[0]


        for ii in range(1, M):
            for jj in range(1, N+1):
                dp[ii][jj]=min(dp[ii-1][jj], dp[ii][jj-coins[ii]] + 1 if jj >= coins[ii] else float('inf'))


        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1
