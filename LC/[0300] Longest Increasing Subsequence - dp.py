##########
# 20230604
##########
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp=[1] * N # where dp[ii] indiciate LIS ending @ ii

        LIS = 1
        for ii in range(1, N):
            for jj in range(ii-1, -1, -1):
                if nums[ii] > nums[jj]:
                    dp[ii]=max(dp[ii], 1+dp[jj])
                        
            LIS=max(LIS, dp[ii])
        print(dp)
        return LIS
            
            
            
            

#######################
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
