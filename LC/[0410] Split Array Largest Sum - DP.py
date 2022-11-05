class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        dp[i][k]: min-max_sum for array in nums[:ii+1] and partitioned into K groups
        ----
        dp[i-1]    << calculated
        dp[i][k-1] << calculated
        dp[i][k] = max(dp[i-1][k-1], nums[i])      #nums[i] starting as a new group, so (k-1) group in dp[i-1]
        x x x x x x o
        case I: o can be independent
        case II: o join prior group
                 x x x x x (x o)
                 x x x x (x x o)
                 ...             <<< need to try all combination
        """

        # ii, num of elements: 0, 1, 2, ... N
        # k, number of groups
        """
          0, 1, ... k
        0
        1
        2
        .
        .
        .
        N
        """
        N=len(nums)
        dp=[([float('inf')]+[float('inf')]*k) for _ in range((N+1))]
        nums=[0]+nums

        dp[0][0]=0
        for ii in range(1, N+1):
            for kk in range(1, min(k, ii)+1): # 1 group was pre-processed
                sum=0
                for jj in reversed(range(kk, ii+1)):
                    sum += nums[jj]
                    dp[ii][kk] = min(dp[ii][kk], max(dp[jj-1][kk-1], sum))

        return dp[-1][-1]
        
