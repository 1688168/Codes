class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        """
        1. for each x
        """
        N = len(s)
        s = list(s)
        processed_cnt = 0
        ans = 0
        for ii in range(N//2):
            jj = N - 1 - processed_cnt
            while jj >= 0 and s[jj] != s[ii]:
                jj -= 1

            # is this the center char?
            if ii == jj:
                kk = N//2-jj
                ans += kk
            else:
                kk = N-1-processed_cnt-jj
                processed_cnt += 1
                ans += kk
                while kk > 0:

                    s[jj], s[jj+1] = s[jj+1], s[jj]

                    kk -= 1
                    jj += 1

        return ans
