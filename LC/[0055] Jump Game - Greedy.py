#############
# 20230611
#############

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N=len(nums)
        dp=[0]*N #the max one can achieve at index ii

        maxSoFar=0
        for ii, vv in enumerate(nums):
            if maxSoFar >= ii:
                maxSoFar = max(ii+nums[ii], maxSoFar)
            else:
                break
        
        return maxSoFar >= N-1


####################

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        N=len(nums)
        greatest_can_reach=nums[0]

        for ii, vv in enumerate(nums):
            if ii > greatest_can_reach: return False

            greatest_can_reach=max(greatest_can_reach, ii+vv)


        return greatest_can_reach >= (N-1)
        
