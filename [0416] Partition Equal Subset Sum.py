from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ttl=sum(nums)
        if ttl%2 != 0: return False
        target=ttl//2
        N=len(nums)

        @lru_cache(None)
        def dp(st, tgt):
            if tgt < 0 or st >=N: return False
            if tgt==0: return True

            return dp(st+1, tgt-nums[st]) or dp(st+1, tgt)


        return dp(0, target)
