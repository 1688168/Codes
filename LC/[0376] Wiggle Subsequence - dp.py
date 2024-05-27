class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up=1 #dp max wiggle len ending @ up slope
        dn=1 #dp max wiggle len ending @ down slope
        N=len(nums)
        for ii in range(1, N):
            if nums[ii] > nums[ii-1]: up = dn + 1
            if nums[ii] < nums[ii-1]: dn = up +1
        
        return max(up, dn)