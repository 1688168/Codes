class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N = len(s)
        M = len(t)
        jj = 0
        for ii in range(N):
            while jj < M and t[jj] != s[ii]:
                jj += 1

            if jj >= M:
                return False
            jj += 1

        return True
