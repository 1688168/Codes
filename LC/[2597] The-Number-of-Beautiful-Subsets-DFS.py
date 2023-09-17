class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        N = len(nums)

        def dfs(st):

            if st >= N:
                return 1

            has_prior_diff_k = False
            for ii in range(st):
                if ii in status and (abs(nums[ii]-nums[st]) == k):
                    has_prior_diff_k = True
                    break

            if has_prior_diff_k:
                return dfs(st+1)
            else:
                no_take = dfs(st+1)
                status.add(st)
                take = dfs(st+1)
                status.remove(st)
                return take+no_take

        status = set()
        return dfs(0)-1