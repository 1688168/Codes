class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []
        nums.sort()

        def helper(sz, st, path):
            if len(path) >= sz:
                res.append(path)
                return

            for ii in range(st, N):
                if ii > st and nums[ii] == nums[ii-1]:
                    continue
                helper(sz, ii+1, path+[nums[ii]])

        for sz in range(N+1):
            path = []
            helper(sz, 0, path)

        return res
