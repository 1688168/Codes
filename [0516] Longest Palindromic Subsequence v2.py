class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        : s => longest palindromic subsequence's length
        : bruteforce:
        : 1. all subsequence: each char is select or not select => 2^n
        : 2. is palindrom: O(N) for each sub-sequence
        : 3. output the longest sub-sequence palindrom
        : ---------------
        : x x x ii x x jj x x
        : dp[ii][jj] = longest palindromic subsequence with ending index window on (ii, jj)
        : dp[ii][jj] = 2 + dp[ii+1][jj-1] if s[ii]=s[jj]
        :       else = max(dp[ii+1][jj], dp[jj-1][ii])
        :
        """
        # state table
        N = len(s)
        s = '#' + s

        dp = [[0] * (N + 1) for _ in range(N + 1)]

        for ii in range(1, N + 1):
            dp[ii][ii] = 1

        # we are considering the window
        for length in range(2, N + 1):  # x x x x x x x: len=2. 7-2+1=6
            for ii in range(1, N - length + 2):
                jj = ii + length - 1
                if s[ii] == s[jj]:
                    dp[ii][jj] = (2 + dp[ii + 1][jj - 1])
                else:
                    dp[ii][jj] = max(dp[ii + 1][jj], dp[ii][jj - 1])
        # print(dp)
        return dp[1][N]