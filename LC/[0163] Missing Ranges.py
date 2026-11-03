class Solution:
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        res=[]

        N=len(nums)

        # handle empty inputs
        if N==0: return [[lower, upper]]

        ii, left, right = 0, 0, 0
 
        # handle begin
        if lower != nums[0]:
            res.append([lower, nums[0]-1])

        for i in range(N - 1):
            left = nums[i] + 1
            right = nums[i + 1] - 1
            if left <= right:
                res.append([left, right])

        if nums[-1] < upper:
            res.append([nums[-1] + 1, upper])

        return res