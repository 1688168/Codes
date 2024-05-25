class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        * nums[ii]=value @ house ii
        * N=100
        * constraint: relating to prev house -> type I DP
        * max monney
        """
        N=len(nums)
        def dfs(st, ttl, prev):
            if st >=N:
                return ttl
            
            if prev is None or prev < st-1:
                return max(dfs(st+1, ttl+nums[st], st), dfs(st+1, ttl, prev))
            else:
                return dfs(st+1, ttl, prev)
        
        return dfs(0, 0, None)
