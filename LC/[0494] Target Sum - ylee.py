class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        target 0 1 ... target
        0
        n1
        n2
        .
        .
        .
        n

        => number of diff expressions that we can build
        dp[ii][jj]: using up to nums[ii]. the number of way to achieve jj

        Knapsack problem.
        1. constrain: target (when you have constrain including negative number, transform to 0 index)
        2. list of items
        3. actions: + or - on each iteam
        4. num of ways
        """
        nums = [0]+nums
        M = len(nums)
        offset = 1000
        N = 2005
        dp = [[0]*N for _ in range(M)]
        dp[0][offset] = 1

        for ii in range(1, M):
            for jj in range(-1000, 1001):

                # if we are adding new number
                if 0 <= jj+offset-nums[ii] <= 2001:
                    dp[ii][jj+offset] += dp[ii-1][jj+offset-nums[ii]]

                # if we are substracting new number
                if 0 <= jj+offset+nums[ii] <= 2002:
                    dp[ii][jj+offset] += dp[ii-1][jj+offset+nums[ii]]

        return dp[-1][target+offset]
