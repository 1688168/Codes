class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        * nums[ii]: profit/cost, always take
        * target: min cost/max profit, target profit
        -> how many ways to sum to target
        """
        N=len(nums)
        
        # dp[ii][jj]: number of ways sum to jj using up to resource ii
        dp=[[0]*2005 for _ in range(N+1)] # [0, N]
        offset=1000
        nums=[0]+nums #insert dummy header for resource
        dp[0][0+offset]=1 #initialize dp
        
        for ii in range(1, N+1): # [1, N]
            for jj in range(-1000, 1001, 1): # [taret, target]
                # take as positive
                if -1000 <= jj-nums[ii] <= 1000:
                    dp[ii][jj+offset] += dp[ii-1][jj-nums[ii]+offset] 

                # take as negative
                if -1000 <= jj+nums[ii] <= 1000:
                    dp[ii][jj+offset] += dp[ii-1][jj+nums[ii]+offset]
        
        return dp[N][target+offset]

        