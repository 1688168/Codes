class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        xx=0
        for nn in nums:
            xx^=nn
        
        return xx
        