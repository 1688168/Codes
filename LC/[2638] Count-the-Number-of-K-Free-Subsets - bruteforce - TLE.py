class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        """
        - get all subsets, skip if  not k-free
        """
        N = len(nums)
        cnt = 0

        def dfs(st, length, subset):
            nonlocal cnt
            if len(subset) == length:
                cnt += 1
                # print(" cnt: ", cnt, " subset: ", subset)
                # res.append(list(subset))
                return

            for ii in range(st, N):
                if nums[ii]-k in subset or nums[ii]+k in subset:
                    continue
                subset.add(nums[ii])
                dfs(ii+1, length, subset)
                subset.remove(nums[ii])

        res = []
        for length in range(N+1):
            subset = set()
            dfs(0, length, subset)

        return cnt
