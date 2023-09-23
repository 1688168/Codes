"""
* genius!
  sum of range = sum(subarray_max-subarray_min) = sum(subarray_max)-sum(subarray_min)
"""

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # int arr
        # range: max-min
        # => sum(all subarray ranges of numd)
        ans=0
        for ii in range(len(nums)):
            mx=nums[ii]
            mn=nums[ii]
            for jj in range(ii+1, len(nums)):
                mx=max(mx, nums[jj])
                mn=min(mn, nums[jj])
                ans += (mx-mn)

        return ans


######################
# this is TLE: O(N^3)
######################
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        N=len(nums)
        ttl_range=0
        for ii in range(N):
            for jj in range(ii+1, N):
                ttl_range += (max(nums[ii:jj+1]) - min(nums[ii:jj+1]))
                # mx=max(nums[ii:jj])
                # mn=min(nums[ii:jj])
                # ttl_range += (mx-mn)
                # print(" ii: ", ii, " jj: ", jj, " mx: ", mx, "mn: ", mn, " ttl: ", ttl_range)
        
        return ttl_range
        