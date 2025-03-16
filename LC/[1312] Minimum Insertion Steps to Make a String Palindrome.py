class Solution:
    def minInsertions(self, s: str) -> int:
        # min insert to make s a palindrome
        # let ss be the reverse of s
        ss=s[::-1]
        # min insert to make s a palindrome is the len-diff of "min super-sequence of s and ss" and s

        N=len(s)
        s= "#" + s
        ss = "#" + ss

        # declare dp
        dp = [[math.inf//2 for _ in range(N+1)] for _ in range(N+1)]
        
        # initialize dp
        for ii in range(1, N+1): dp[ii][0] = ii
        for jj in range(1, N+1): dp[0][jj] = jj

        dp[0][0] = 0

        # populate dp
        for ii in range(1, N+1):
            for jj in range(1, N+1):
                if s[ii]==ss[jj]:
                    dp[ii][jj] = dp[ii-1][jj-1]+1
                else:
                    dp[ii][jj] = min(dp[ii-1][jj], dp[ii][jj-1]) + 1

        return dp[-1][-1] - N
        