class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)

        def helper(st, nums):
            if st == N:
                res.append(nums)
                return

            for ii in range(st, N):
                # fix st and swap with all
                nums[st], nums[ii] = nums[ii], nums[st]
                helper(st+1, nums[:])  # next will be fixing st+1
                nums[st], nums[ii] = nums[ii], nums[st]

        helper(0, nums)

        return res
