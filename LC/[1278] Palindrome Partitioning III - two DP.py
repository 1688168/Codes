class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        """
        # optimizing something
        * binary search
        * greedy
        * DP
        * search
        """

        N=len(s)

        s ='#'+ s
        """
        dp[ii][kk]=min edit required for s[1:ii+1] and kk partitions
        dp[ii][kk] = min(dp[ii][kk], x+dp[jj-1][kk-1]) for jj in range(kk, ii)
        """
        dp0 = [[0]*(N+1) for _ in range(N+1)]
        
        for ll in range(2, N+1): # type 5 DP
            for ii in range(1, N-ll+2):
                jj=ii+ll-1
                dp0[ii][jj] = dp0[ii+1][jj-1] + (1 if s[ii]!= s[jj] else 0)


        dp=[[math.inf]*(k+1) for _ in range(N+1)]
        dp[0][0]=0

        
        """
        x x x x
        k=3

        """

        for ii in range(1, N+1): #for each char as last char of last partition
            for kk in range(1, min(ii+1, k+1)): # for each partion cnt
                for jj in range(kk-1, ii+1):
                    dp[ii][kk] = min(dp[ii][kk], dp0[jj][ii] + dp[jj-1][kk-1])

        #print(dp)

        return dp[-1][-1]

        