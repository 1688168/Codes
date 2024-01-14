class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # find the largest prefix sum
        nums = nums+[0]
        N = len(nums)

        if N == 2:
            return nums[0]+1

        for ii in range(1, N):
            if nums[ii] != nums[ii-1]+1:
                break

        ttl = sum(nums[:ii])
        # print(" ttl: ", ttl)

        # find the smallest missing num
        nums_set = set(nums)

        nxt_num = ttl
        for nn in range(nxt_num, 5000):
            if nn not in nums_set:
                break

        return nn
