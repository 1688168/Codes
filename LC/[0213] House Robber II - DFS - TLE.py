class Solution:
    def rob(self, nums: List[int]) -> int:
        N=len(nums)
        def dfs(is_first, prev, st, ttl):
            if st >= N: return ttl

            if st==N-1 and is_first: return dfs(is_first, prev, st+1, ttl)
                     
            if prev is None or st-1 > prev:
                return max(dfs(is_first, st, st+1, ttl+nums[st]), dfs(is_first, prev, st+1, ttl))                
            else:
                return dfs(is_first, prev, st+1, ttl)
        
        return max(dfs(True, 0, 1, nums[0]), dfs(False, None, 1, 0))