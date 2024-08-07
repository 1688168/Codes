class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        """
        * n: members
        * profit[ii]: profit @ iith resource
        * group[ii]: required cost for iith resource
        * minProfit
        * -> num of ways to achive minProfit
        """
        MAX_GROUP_LEN=105
        M = int(1e9)+7
        N=len(group)
        group = [0]+group
        profit = [0]+profit

        # declare dp s.t. dp[ii][jj][kk]: the number of ways that we can achieve
        # minProfit=kk
        # using only jj ppl
        # @ project ii
        """
        dp[ii+1][jj][kk] += dp[ii][jj][kk]
        dp[ii+1][jj+group[ii+1]][kk+profit[ii+1]]
        """
        dp = [[[0]*(minProfit+2) for _ in range(n+2)] for _ in range(MAX_GROUP_LEN)]
        dp[0][0][0]=1

        # so we need to start from zero cuz we are inferring ii+1 (the opposite direction)
        for ii in range(N+1): #for each project, we DONOT need to cover Nth proj, as we do not need to infer anything beyound last project
            for jj in range(n): 
                for kk in range(minProfit+1):
                    dp[ii+1][jj][kk] = (dp[ii+1][jj][kk] + dp[ii][jj][kk])%M

                    if jj+group[ii+1] <= n:
                        dp[ii+1][jj+group[ii+1]][min(minProfit, kk+profit[ii+1])] = (dp[ii+1][jj+group[ii+1]][min(minProfit, kk+profit[ii+1])]+ dp[ii][jj][kk])%M
        
        ans=0
        for jj in range(n+1):
            ans = (ans + dp[-1][jj][minProfit])%M
        
        return ans