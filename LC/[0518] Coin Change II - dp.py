# [20220924]
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        dp[ii][jj]: the number of combinations using upto ii coin to make up jj amt
        dp[0][0]=1
        dp[ii][jj] = dp[ii-1][jj]+dp[ii][jj-coin[ii]]
        """
        if amount == 0: return 1
        if len(coins)==0: return 0

        dp=[[0]*(amount+1) for _ in range(len(coins))]


        for ii in range(1, amount+1):
            dp[0][ii]= (1 if ii%coins[0]==0 else 0)

        for ii in range(len(coins)):
            dp[ii][0]=1



        for ii in range(1, len(coins)):
            for jj in range(amount+1):
                dp[ii][jj]=dp[ii-1][jj] + (dp[ii][jj-coins[ii]] if jj >=coins[ii] else 0)



        return dp[-1][-1]
