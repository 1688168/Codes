class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N1=len(s1)
        N2=len(s2)
        if N1+N2 != len(s3): return False
        
        s1 = "#"+s1
        s2 = "#"+s2
        s3 = "#"+s3
        
        dp = [[False]*(N2+1) for _ in range(N1+1)]

        # initializing dp values
        """
        # we know N1+N2 = len(S3) per above check.

        """
        dp[0][0]=True # 3 null string
        for ii in range(1, N1+1): dp[ii][0] = (dp[ii-1][0] and s1[ii]==s3[ii]) # s2 is null
        for jj in range(1, N2+1): dp[0][jj] = (dp[0][jj-1] and s2[jj]==s3[jj]) # s2 is null

        """
        dp[ii][jj]: can s1[:N1+1] and s2[:N2+1] interleave S3[:N1+N2+1]

        """
        for ii in range(1, N1+1):
            for jj in range(1, N2+1):
                if dp[ii-1][jj] and s1[ii]==s3[ii+jj]: # anything you ref here need to be initialized
                    dp[ii][jj] = True
                elif dp[ii][jj-1] and s2[jj]==s3[ii+jj]:
                    dp[ii][jj] = True
        
        return dp[-1][-1]
                
        