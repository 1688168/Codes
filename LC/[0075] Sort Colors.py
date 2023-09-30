class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        ll, ii, rr = 0, 0, N-1

        while ii <= rr:
            if nums[ii] == 0:  # Red
                nums[ii], nums[ll] = nums[ll], nums[ii]
                ii += 1
                ll += 1
            elif nums[ii] == 1:  # White
                ii += 1
            else:  # Blue
                nums[ii], nums[rr] = nums[rr], nums[ii]
                rr -= 1
