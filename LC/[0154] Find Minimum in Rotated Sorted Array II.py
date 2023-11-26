class Solution:
    def findMin(self, nums: List[int]) -> int:
        while len(nums) > 1 and nums[-1] == nums[0]:
            nums.pop()
        if nums[0] < nums[-1]:
            return nums[0]

        ll, rr = 0, len(nums)-1
        ans = -1

        while ll <= rr:
            mm = ll+(rr-ll)//2

            if nums[mm] < nums[0]:
                ans = mm
                rr = mm-1
            else:
                ll = mm+1

        return nums[ans]
