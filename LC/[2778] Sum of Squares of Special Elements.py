class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        sum=0
        n=len(nums)
        for ii, vv in enumerate(nums):
            if (n % (ii+1)) == 0:
                sum += pow(vv, 2)
        
        return sum