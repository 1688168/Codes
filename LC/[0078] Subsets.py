class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def helper(sz, st, path):
            if st == sz:
                res.append(path[:])
                return
            if st > sz:
                return

            for ii in range(st, len(nums)):
                helper(sz, ii+1, path+[nums[ii]])

        res = []
        for sz in range(len(nums)+1):  # try diff size from 0~nn: O(N)
            path = []

            helper(sz, 0, path)

        return res
