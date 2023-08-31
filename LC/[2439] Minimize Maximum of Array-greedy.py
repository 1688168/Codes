class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        total=0
        res=nums[0]
        for ii in range(len(nums)):
            total+= nums[ii]
            res = max(res, math.ceil(total/(ii+1)))        

        return res