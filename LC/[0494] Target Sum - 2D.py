class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums = [0]+nums
        M = len(nums)
        N = 2005
        offset = 1000
        """ -1000, -999, ..., 0, 1, 2, ..., 1000
        0  
        n1
        n2
        n3 
        .
        .
        .
        """

        dp = [[0]*N for _ in range(M)]
        dp[0][0+offset] = 1

        for ii in range(1, M):
            for jj in range(-1000, 1001):
                # we are only interested in sum between (-1000, 1000). anything outside of that we are not interested
                # we only need to worry about those with sum in range
                if jj-nums[ii] <= 1000 and jj-nums[ii] >= -1000:
                    dp[ii][jj+offset] += dp[ii-1][jj-nums[ii]+offset]

                if jj+nums[ii] <= 1000 and jj+nums[ii] >= -1000:
                    dp[ii][jj+offset] += dp[ii-1][jj+nums[ii]+offset]

        return dp[-1][target+offset]
