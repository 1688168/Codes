class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        : nums(int)
        : dp[ii] - len of longest increasing subsequence ending @ ii
        : dp[ii] = dp[ii-1]
        """
        N=len(nums)
        dp=[1]*N
        mxl=1

        for ii in range(N):
            for jj in range(ii):
                dp[ii]=max(dp[ii], (dp[jj]+1) if nums[ii] > nums[jj] else 1)
            mxl=max(mxl, dp[ii])

        return mxl
