class Solution:
    def numDecodings(self, s: str) -> int:
        """
        this is like climbing stairs
        -> how many unique ways you can reach the top
           * each time you can climb 1 stair or two stairs
        -> how many unique ways you can reach the string to decode it?
           * each time you can decode one char or two chars
           * some additional constrans to decode two chars
        """
        N=len(s)
        dp={N: 1}

        def dfs(ii):
            if ii in dp: return dp[ii]
            if s[ii]=='0': 
                dp[ii]=0
                return dp[ii]
            

            res=dfs(ii+1) # no special constrain a single char

            if ii+1 < N and int(s[ii]) < 3 and not (s[ii]=='2' and int(s[ii+1])> 6):
                res += dfs(ii+2)

            dp[ii]=res
            return dp[ii]
        

        return dfs(0)
        

##########################

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
