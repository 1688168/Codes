############
# 20240814
############
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
        
        for ii in range(1, N+1): #from 1~N (after dummy insertion)
            for jj in range(k):  #sum from 0~(k-1)
                dp[ii][jj] = (dp[ii][jj] + dp[ii-1][jj])%M
                if jj >= nums[ii]:
                    dp[ii][jj] = (dp[ii][jj] + dp[ii-1][jj-nums[ii]])%M
        
        ttl = pow(2, N)%M
        invalid = sum(dp[N])%M

        return (ttl-invalid*2%M)%M


############
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        """
        nums: postive int
        two groups:
        group sum > k
        """
        MOD = int(1e9+7)
        nums = [0]+nums
        M = len(nums)
        N = k+1
        if sum(nums) < 2*k:
            return 0
        dp = [[0]*N for _ in range(M)]
        """
        # dp[ii][jj]: consider first iith elements in nums, how many diff partitions s.t. the sum of each group is jj
        x x x x x x ii
        dp[ii][s] = dp[ii-1][s] + dp[ii-1][s-nums[ii]]

        ans = 2^n - sum(dp[n][0]+dp[n][1]+...+dp[n][k-1]) # this is num of partitions s.t. sum(group1) >= k
                  - num of partitions s.t. sum(group1) >= k and sum(group2) < k --- B
    
        B -- num of partitions s.t. sum(group1) >= k and sum(group2) < k
          => num of partitions s.t. sum(group2) < k (remember we required ttl_sum >= 2k)
          => num of partitions s.t. sum(group1) < k (A and B are symmetric) -- C
        so ttl=pow(2, k) - 2*B

        ====
        ttl grouping count: power(2, len(nums))
        
        valid_cnt = ttl_count - 2*invalid_group1 (since invalid group1_cnt and invalid group2_cnt are the same)
        """

        dp[0][0] = 1

        for ii in range(1, M):
            for jj in range(N):  # jj=individual group sum

                dp[ii][jj] += dp[ii-1][jj]

                if jj >= nums[ii]:
                    dp[ii][jj] += dp[ii-1][jj-nums[ii]]

                dp[ii][jj] %= MOD

        invalid_cnt = 0
        for ss in range(N-1):
            invalid_cnt += dp[-1][ss]

        ttl = int(pow(2, M-1)) % MOD
        # ttl=1
        # for ii in range(1, M):
        #     ttl = ttl * 2 % MOD
        return (ttl - invalid_cnt-invalid_cnt) % MOD
