class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        N=len(nums)
        # declare dp
        dp=[float('-inf')]*N # where dp[ii]=max score we can reach @ idx=ii
        dp[0]=nums[0]

        for ii in range(N):
            for jj in range(ii+1, min(ii+k+1, N)):
                dp[jj] = max(dp[jj], dp[ii]+nums[jj])
        # print(dp)
        return dp[-1]


# * N=10^5 -> NlogN
# * let dp[ii] max score you can reach @ ii
# * dp[ii] = max(dp[ii], dp[jj]+nums[ii]) for jj in "k"
        