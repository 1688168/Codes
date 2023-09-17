class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ii, jj = 0, 0
        ns, nt = len(s), len(t)

        while ii < ns and jj < nt:
            cs = s[ii]

            ct = t[jj]
            if cs == ct:
                jj += 1

            ii += 1

        return nt-jj
