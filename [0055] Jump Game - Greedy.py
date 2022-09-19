class Solution:
    def canJump(self, nums: List[int]) -> bool:
        greatest_can_reach=0

        for ii, vv in enumerate(nums):
            if ii > greatest_can_reach: return False

            greatest_can_reach=max(greatest_can_reach, ii+nums[ii])


        return True if greatest_can_reach >= len(nums)-1 else False
        
