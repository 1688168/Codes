class Solution:
    def canJump(self, nums: List[int]) -> bool:

        N=len(nums)
        greatest_can_reach=nums[0]

        for ii, vv in enumerate(nums):
            if ii > greatest_can_reach: return False

            greatest_can_reach=max(greatest_can_reach, ii+vv)


        return greatest_can_reach >= (N-1)
        
