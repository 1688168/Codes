##############
# 20240511
##############
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        # Given nums
        + LIS @ ii has to do with LIS @ jj where jj < ii and nums[jj] < nums[ii]
        dp[ii]: LIS @ ii
              = dp[jj]+1 if nums[jj]<nums[ii]
        """
        nums = [math.inf]+nums # insert dummay header since we need to ref to ii-1
        N=len(nums)

        dp=[1]*N

        for ii in range(1, N):
            for jj in reversed(range(1, ii)):
                if nums[jj] >= nums[ii]: continue
                dp[ii] = max(dp[ii], dp[jj]+1)
        
        return max(dp)
        
##############
# 20240429
##############
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        dp[ii]: longest increasing subsequence ending @ ii
        dp[ii] = max(dp[jj]+1 if nums[ii]>nums[jj] else dp[ii])
        """
        N=len(nums)
        dp=[1]*N

        for ii, nn in enumerate(nums):
            if ii==0: continue
            for jj in range(ii-1, -1, -1):
                if nums[jj] < nn:
                    dp[ii]=max(dp[ii], dp[jj]+1)
                    
        return max(dp)
        

##########
# 20231226
##########
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        dp[ii] = dp[jj] + 1 where jj in [:ii]
        """

        N = len(nums)
        dp = [1]*N

        mxl = 0
        for ii in range(N):
            if ii == 0:
                dp[ii] = 1
                mxl = max(dp[ii], mxl)
                continue

            jj = ii-1

            while jj >= 0:
                dp[ii] = max(
                    dp[ii], (dp[jj] if nums[jj] < nums[ii] else 0) + 1)
                mxl = max(dp[ii], mxl)
                jj -= 1

        return mxl
##########
# 20230604
##########


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N  # where dp[ii] indiciate LIS ending @ ii

        LIS = 1
        for ii in range(1, N):
            for jj in range(ii-1, -1, -1):
                if nums[ii] > nums[jj]:
                    dp[ii] = max(dp[ii], 1+dp[jj])

            LIS = max(LIS, dp[ii])
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
        N = len(nums)
        dp = [1]*N
        mxl = 1

        for ii in range(N):
            for jj in range(ii):
                dp[ii] = max(dp[ii], (dp[jj]+1) if nums[ii] > nums[jj] else 1)
            mxl = max(mxl, dp[ii])

        return mxl
