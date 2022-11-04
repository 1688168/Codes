from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:

        N=len(s)
        memo={}
        def dp(st):
            if st in memo: return memo[st]
            if st >= N: return 1
            if int(s[st])==0: return 0


            # single digits
            ans = dp(st+1)

            # two digits
            if st+1 < N and (int(s[st])==1 or (int(s[st])==2 and int(s[st+1]) <= 6)):
                ans += dp(st+2)
            memo[st]=ans
            return memo[st]
        
        return dp(0)
