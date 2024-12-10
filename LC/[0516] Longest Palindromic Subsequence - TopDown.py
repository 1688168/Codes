class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        @cache
        def lps(st, ed):
            if st==ed: return 1
            if st > ed: return 0

            if s[st]==s[ed]: 
                return 2+lps(st+1, ed-1)
            else:
                return max(lps(st+1, ed), lps(st, ed-1))
        
        return lps(0, len(s)-1)
        