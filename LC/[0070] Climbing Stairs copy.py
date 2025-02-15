from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        @lru_cache(None)
        def dp(n):
            if n<=1: return 1            
            return dp(n-1)+dp(n-2)            
            
            
        return dp(n)
    

########################
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        pre=2
        prepre=1
        cnt = 0
        for ii in range(3, n+1):
            cnt = prepre+pre
            prepre=pre
            pre=cnt
        

        return cnt
        