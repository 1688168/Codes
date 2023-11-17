class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        res = []

        def helper(st, nums):
            if st >= N:
                res.append(nums)
                return

            used = set()
            for ii in range(st, N):
                if nums[ii] in used:  # we pick a num to be in the starting position.  if this number was used before, we just skip to avoid duplicate
                    continue
                used.add(nums[ii])
                nums[st], nums[ii] = nums[ii], nums[st]
                helper(st+1, nums[:])
                nums[st], nums[ii] = nums[ii], nums[st]

        helper(0, nums)

        return res
