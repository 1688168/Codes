from bisect import bisect_left, bisect_right


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        cnt = 0
        for ii, vv in enumerate(nums):
            # if ii == 0: continue
            # find the range that as i that nums[i]+nums[j] in (lower, upper)
            """
            vv+nums[ii]>= lower
            nums[ii]>= lower-vv

            vv+nums[ii] <= upper
            nums[ii] <= upper - vv
            """
            # start = bisect_left(nums[:ii+1], lower-vv)
            # end = bisect_right(nums[:ii+1], upper-vv)
            start = bisect_left(nums, lower-vv)
            end = bisect_right(nums, upper-vv)
            cnt += (end-start)
            if lower <= vv*2 <= upper:
                cnt -= 1

            # print(" ii: ", ii, " start :", start, " end:", end, " cnt: ", cnt)
        return cnt//2


# this python is TLE


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        cnt = 0
        for ii, vv in enumerate(nums):
            if ii == 0:
                continue
            # find the range that as i that nums[i]+nums[j] in (lower, upper)
            """
            vv+nums[ii]>= lower
            nums[ii]>= lower-vv

            vv+nums[ii] <= upper
            nums[ii] <= upper - vv
            """
            start = bisect_left(nums[:ii+1], lower-vv)
            end = bisect_right(nums[:ii+1], upper-vv)
            cnt += (end-start)
            if lower <= vv*2 <= upper:
                cnt -= 1

            # print(" ii: ", ii, " start :", start, " end:", end, " cnt: ", cnt)
        return cnt
