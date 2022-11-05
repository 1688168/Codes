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
        N=len(nums)
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
        dp=[([0]+[0]*k) for _ in range((N+1))]
        nums=[0]+nums
        #dp[0][0]: zero elements and partition into zero groups -> min-max_sum=0
        #dp[0][0]=0


        # if we only have 1 group, the min-max_sum for each ii is the sum of all items so far
        for ii in range(1, N+1): # if you only have one group, the min-max_sum is the sum of all
            dp[ii][1] = dp[ii-1][1] + nums[ii]  # 1 group -> presum

        #print(dp)

        for ii in range(1, N+1):
            for kk in range(2, min(k, ii)+1): # 1 group was pre-processed

                # case I, self form a group, with prior k-1 groups
                dp[ii][kk] = max(dp[ii-1][kk-1], nums[ii]) # form a new group yourself

                for jj in range(1, ii): # join with previous, need to try all combination
                    tmp=max(dp[jj][kk-1], dp[ii][1]-dp[jj][1])# presum
                    dp[ii][kk]=min(dp[ii][kk], tmp)

        # for ii, nn in enumerate(nums, 1): # ii: 1~len(nums), for each number of element
        #     for kk in range(min(k, ii)+1): # we can partition to ii groups (1 in each group) as max
        #         dp[ii][kk] = max(dp[ii-1][kk-1], nn)
        #         sum=0
        #         for jj in range(1, ii):
        #             tmp=max(dp[jj][kk-1], dp[ii][1]-dp[jj][1])
        #             #dp[ii][kk] = min(dp[ii][kk], max(dp[jj-1][kk-1], sum))



        return dp[-1][-1]
