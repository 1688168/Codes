########
# 20240505
########
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        N=len(nums)
        nums.sort()
        dp = [1] * N
        prev = [-1] * N

        for ii in range(N):
            for jj in reversed(range(ii)):
                if nums[ii]%nums[jj]==0:
                    dp[ii]=max(dp[ii], dp[jj]+1)
                    if dp[ii]==dp[jj]+1: # we have a larger subset
                        prev[ii]=jj #record the path for trace back
        

        #figure out which ii has the max length
        mxl=0
        idx=-1
        for ii in range(N):
            if dp[ii] > mxl:
                mxl=dp[ii]
                idx=ii

        res=[]
        while idx != -1:
            res.append(nums[idx])
            idx=prev[idx]

        return res
        
#####################
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        N = len(nums)  # take measurement

        nums.sort()  # sorted in increasing order inplace

        dp = [1]*N  # dp[ii] the size of max divisible subset ending @ ii
        prev = [-1]*N  # record the prev divisor

        lds = 0  # global largest divisible subset
        ldsi = 0  # the index of teh largest divisible subset end
        res = []  # elements of the largest divisible subset

        for ii, nn in enumerate(nums):
            for jj in range(ii):
                if nums[ii] % nums[jj] != 0:
                    continue  # ii is bigger

                if 1+dp[jj] > dp[ii]:
                    dp[ii] = 1+dp[jj]
                    prev[ii] = jj

            if dp[ii] > lds:
                lds = dp[ii]
                ldsi = ii

        ii = ldsi

        while ii != -1:
            res.append(nums[ii])
            ii = prev[ii]
        return res
