class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        """
        - subarray
        - sum(subarray(mx-mn))
        - sum(mx*contribution)-sum(mn*contribution)
          where contribution is num of subarrays which mx/mn can be max/min
        """
        # let's try one pass

        nums_orig = nums[:]
        nums = [math.inf]+nums+[math.inf]

        # calc max sum
        stk = []
        ttl = 0
        for ii, vv in enumerate(nums):
            while stk and vv > nums[stk[-1]]:
                curr_ii = stk.pop()
                prev_ii = stk[-1]
                ttl += (ii-curr_ii)*(curr_ii-prev_ii)*nums[curr_ii]

            stk.append(ii)

        print(" ttl: ", ttl)
        # calc min
        nums = [-math.inf]+nums_orig+[-math.inf]
        stk = []
        for ii, vv in enumerate(nums):
            while stk and vv < nums[stk[-1]]:
                curr_ii = stk.pop()
                prev_ii = stk[-1]
                ttl -= (ii-curr_ii)*(curr_ii-prev_ii)*nums[curr_ii]

            stk.append(ii)

        return ttl
