class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        """
        - S: divide S into K 
        - k:
        - N: ?
        => min num of chars need to change
        * 无后效性
        dp[ii][kk]: the minimal number of characters that you need to change to divide the string s[:ii+1] into k substrings that are all palindromes

        * consider s[0:ii+1], divide this substring into k substring

        {xxxxxx}[jxxx ii] # => min(dp[jj-1][k-1] + helper(s[j:ii+1])) for jj=1,2,3...ii
        k-1     | last one                     ^^^^^^^^^^^^^^^
                                               required flips to make last interval palindrome

        for ii in range(1, N):
            for k in range(1, min(KK, ii+1))
                for jj in range(k, ii+1): # k intervals, jj is the start of the last interval
                    dp[ii][kk]=dp[jj-1][k-1] + helper(s, jj, ii)

        return dp[-1][-1]
        """
        s = '#'+s
        N = len(s)
        dp = [[math.inf]*(k+1) for _ in range(N)]
        dp[0][0] = 0

        memo = {}

        def helper(s, st, ed):
            if (st, ed) in memo:
                return memo[(st, ed)]
            ll, rr = st, ed
            cnt = 0
            while ll < rr:
                if s[ll] != s[rr]:
                    cnt += 1
                ll += 1
                rr -= 1
            memo[(st, ed)] = cnt
            return cnt

        for ii in range(1, N):
            for kk in range(1, min(k+1, ii+1)):
                for jj in range(kk, ii+1):  # k intervals, jj is the start of the last interval
                    # try cache helper for optimization
                    dp[ii][kk] = min(dp[ii][kk], dp[jj-1]
                                     [kk-1] + helper(s, jj, ii))

        return dp[-1][-1]
