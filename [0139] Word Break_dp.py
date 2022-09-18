class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        : 1. string matching -> Trie lookup
        : 2. if existing -> potentially DP
        : dp[ii]: if string length=ii can be broken
          dp[0]: if string length=0 is True
        """
        N = len(s)
        dp = [False] * (N + 1)  # length can be 0...N
        dp[0] = True

        for ii in range(1, N + 1):  # length from 1...N     s[:jj] from dp, s[jj:] in dictionary
            for jj in range(ii + 1):  # length from 0...ii
                """
                ij   : 0,   1,    2
                s[ii]: 0:1, none, 
                """
                dp[ii] = dp[jj] and (s[jj:ii] in wordDict)
                if dp[ii]: break

        return dp[N]