class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N=len(nums)
        if N <=1: return [nums]
        res=[]
        def helper(st, nums):
            if st==N:
                res.append(nums[:])
                return
            if st > N: return None

            for ii in range(st, N):
                nums[st], nums[ii] = nums[ii], nums[st]
                helper(st+1, nums)
                nums[st], nums[ii] = nums[ii], nums[st]
        

        helper(0, nums)
        return res