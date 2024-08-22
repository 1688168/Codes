class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        * Group A: take as positive
        * Group B: anything not in group A are negative
        * Total: sum(nums)

        * TotalA: sum(A)
        * TotalB: -1*(Total-A)
        * target=sum(A)+sum(B)
        """
        N=len(nums)
        nums=[0]+nums

        """
        dp[ii][jj]: num of ways sum(A)=jj using up to ii elements all taking as positive
        """
        dp=[[0]*(1005) for _ in range(N+1)]
        dp[0][0]=1

        total = sum(nums)

        for ii in range(1, N+1): #[1, N]
            for jj in range(0, 1001):
                dp[ii][jj] = dp[ii-1][jj] # skip nums[ii]
                if 0 <= jj - nums[ii] <= 1000: # take nums[ii]
                    dp[ii][jj] += dp[ii-1][jj-nums[ii]]
        
        """
        A + B = target
        total = A - B
        B = A-Total

        A + A-Total = Target
        2A=target+total
        A=(target+total)//2
        """
        if target > total: return 0
        if (target+total) %2 != 0: return 0
        A = (target+total)//2

        return dp[N][A]