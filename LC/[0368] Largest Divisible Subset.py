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
