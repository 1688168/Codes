############
# 20230923
############
# smart way to calc prev_smaller, prev_greaterafse

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        """
        - O(N)
        -> traverse nums for one time
        -> sum(subarray(mx-min))
        -> sum(subarray(mx)) -sum(subarray(mn))
        -> let ii be the element of mx/mn of a subArrayRanges
        -> how many subarrays can use ii as mx/mn?
                                 0 1 2 3 4 5
        -> find the prev/next -> x x x x x x
                                 a   i     b
        ->  (b-i)*(i-a)

        """
        N = len(nums)
        prev_smaller_equal = [-1]*N
        next_smaller = [N]*N
        prev_greater_equal = [-1]*N
        next_greater = [N]*N

        stk = []
        for ii in range(N):
            while len(stk) > 0 and nums[ii] < nums[stk[-1]]:
                next_smaller[stk[-1]] = ii
                stk.pop()
            if len(stk) > 0:
                prev_smaller_equal[ii] = stk[-1]
            stk.append(ii)

        stk = []
        for ii in range(N):
            while len(stk) > 0 and nums[ii] > nums[stk[-1]]:
                next_greater[stk[-1]] = ii
                stk.pop()
            if len(stk) > 0:
                prev_greater_equal[ii] = stk[-1]
            stk.append(ii)
        ttl_min = 0
        ttl_max = 0
        for ii in range(N):
            a = ii-prev_smaller_equal[ii]
            b = next_smaller[ii]-ii
            ttl_min += (nums[ii]*a*b)
            a = ii-prev_greater_equal[ii]
            b = next_greater[ii]-ii
            ttl_max += (nums[ii]*a*b)
        return ttl_max - ttl_min


############
# 20230820
############

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        """
        sum(A-B) = sum(a)-sum(b)
        """

        N = len(nums)
        prev_smaller = [-1]*N
        next_smaller = [N]*N
        prev_greater = [-1]*N
        next_greater = [N]*N

        # precalc next smaller
        stk = []
        for ii in range(N):
            while len(stk) > 0 and nums[ii] < nums[stk[-1]]:
                next_smaller[stk[-1]] = ii
                stk.pop()
            stk.append(ii)

        # precalc prev smaller
        stk = []
        for ii in reversed(range(N)):
            while len(stk) > 0 and nums[ii] <= nums[stk[-1]]:
                prev_smaller[stk[-1]] = ii
                stk.pop()
            stk.append(ii)

        # precalc next greater
        stk = []
        for ii in range(N):
            while len(stk) > 0 and nums[ii] > nums[stk[-1]]:
                next_greater[stk[-1]] = ii
                stk.pop()
            stk.append(ii)

        # precalc prev greater
        stk = []
        for ii in reversed(range(N)):
            while len(stk) > 0 and nums[ii] >= nums[stk[-1]]:
                prev_greater[stk[-1]] = ii
                stk.pop()
            stk.append(ii)

        res = 0
        # calc result
        mx_sum = 0
        mn_sum = 0

        """
        0 1 2 3 4 5
            ^
        """

        for ii, vv in enumerate(nums):
            ll = ii-prev_greater[ii]
            rr = next_greater[ii]-ii
            mx_sum += vv*ll*rr

            ll = ii-prev_smaller[ii]
            rr = next_smaller[ii]-ii
            mn_sum += vv*ll*rr

        return mx_sum-mn_sum
