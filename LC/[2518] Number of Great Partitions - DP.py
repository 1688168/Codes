class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        """
        * how do you know this is knapsack problem?
        1. given a list or resource
        2. given a target value
        3. num of ways to select
        * nums[ii]: positive integers
        * k: 
        """
        N=len(nums)
        M=int(1e9)+7
        ttl=sum(nums)

        if ttl < 2* k: return 0 # sanity check as we need both sum(A)>= k and sum(B)>= k
        
        # dp[ii][jj]: number of partitions ending @ iith elements with sum(A) to jj

        dp=[[0]*(k) for _ in range(N)] # we are calc sum < k

        # initialize when ii=0
        dp[0][0] = 1 # sum to zero with first element -> by skipping it
        for jj in range(1, k):
            if jj==nums[0]: dp[0][jj]=1

        for ii in range(1, N):
            for jj in range(k):
                dp[ii][jj] += dp[ii-1][jj]                 
                if jj>= nums[ii]:  dp[ii][jj] +=dp[ii-1][jj-nums[ii]]
        
        ttl_cnt = pow(2, N) % M
        invalid=0
        for jj in range(k):
            invalid = (invalid + dp[-1][jj])%M
        

        return (ttl_cnt - invalid - invalid + M)%M



        