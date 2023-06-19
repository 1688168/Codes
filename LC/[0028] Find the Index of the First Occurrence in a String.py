class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        M = len(haystack)
        N = len(needle)

        if N > M:
            return -1

        """
        M=5
        N=3
        01234
        """
        for ii in range(M-N+1):
            if haystack[ii] != needle[0] or haystack[ii+N-1] != needle[-1]:
                continue
            ll, rr = 0, N-1
            while ll <= rr:
                if haystack[ii+ll] != needle[ll] or haystack[ii+rr] != needle[rr]:
                    break
                ll += 1
                rr -= 1

            if ll > rr:
                return ii

        return -1
