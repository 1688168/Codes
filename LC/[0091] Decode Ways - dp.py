class Solution:
    def numDecodings(self, s: str) -> int:
        N=len(s)
        dp={len(s): 1}

        for ii in range(N-1, -1, -1):
            if int(s[ii])==0:
                dp[ii]=0
            else:
                dp[ii]=dp[ii+1]

            if ii+1 < N and (int(s[ii])==1 or int(s[ii])==2 and int(s[ii+1]) <=6):
                dp[ii]+=dp[ii+2]

        return dp[0]
        
