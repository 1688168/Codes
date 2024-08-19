class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        """
        * nums[ii]: an array of resources
        * when partition to two groups  (A, B), this is equivalent to each item is choose or skip, 
          picked in Group A, skipped (automatically) in Group B
        * whenever you pick/skip something and count ways/optimize profit/cost -> DP
        * whenever you have a big anser space and need MOD -> think of DP
        * whenever you have two partition groups -> consider they are symmentric
        * whenever you have two partitions, think of ttl = A + B 
        """
        N=len(nums)
        M=int(1e9)+7

        if sum(nums) < 2*k: return 0

        nums=[0]+nums # have (N+1) in size 

        dp = [[0]*k for _ in range(N+1)] # N resources (0~N-1). sum to 0~(k-1)     
        dp[0][0]=1
        
        for ii in range(N): #from 1~N (after dummy insertion)
            for jj in range(k):  #sum from 0~(k-1)
                dp[ii+1][jj] = (dp[ii+1][jj]+ dp[ii][jj])%M
                if jj >= nums[ii+1]:
                    dp[ii+1][jj] = (dp[ii+1][jj] + dp[ii][jj-nums[ii+1]])%M
        
        ttl = pow(2, N)%M
        invalid = sum(dp[-1])%M

        return (ttl-invalid*2%M)%M