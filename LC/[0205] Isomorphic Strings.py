class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        N = len(s)
        M = len(t)
        if N != M:
            return False

        s2t = {}
        mapped = set()

        for ii in range(M):
            c1 = s[ii]
            c2 = t[ii]

            if c1 in s2t:
                if s2t[c1] != c2:
                    return False
            else:
                if c2 in mapped:
                    return False
                s2t[c1] = c2
                mapped.add(c2)

        return True
