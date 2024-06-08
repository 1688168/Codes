class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        # I/O:
        + nums[ii]
        + target
        => num of ways to achive target

        # Analysis:
        + N=20

        > Bruteforce:
        = 2^20
        """

        N=len(nums)
        def dfs(st, ttl):
            if st==N and ttl==target: return 1
            if st >=N: return 0

            return dfs(st+1, ttl+nums[st]) + dfs(st+1, ttl-nums[st])
            

        return dfs(0, 0)