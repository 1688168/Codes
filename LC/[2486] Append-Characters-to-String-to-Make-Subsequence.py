#############
# 20240202
#############
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """
        s:
        t:
        """
        NS=len(s)
        NT=len(t)
        ii=jj=0

        while ii < NS and jj < NT:
            while ii < NS and s[ii]!=t[jj]:
                ii+=1
            if ii >= NS: break
            ii+=1
            jj+=1
        
        return NT-jj
        

###################
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
