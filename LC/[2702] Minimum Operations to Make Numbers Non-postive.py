"""
https://www.youtube.com/watch?v=ZBA_PacfEic&t=12s
"""


class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        ll, rr = 0, pow(2, 32)
        ans = -1

        nums.sort(reverse=True)

        def is_feasible(mm):
            count = 0
            for ii in range(len(nums)):
                if nums[ii]-y*mm <= 0:
                    continue
                count += math.ceil((nums[ii] - mm*y)/(x-y))
                if count > mm:
                    return False

            return True

        while ll <= rr:
            mm = ll+(rr-ll)//2

            if is_feasible(mm):
                ans = mm
                rr = mm-1
            else:
                ll = mm+1

        return ans
