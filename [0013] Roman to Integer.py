class Solution:
    def romanToInt(self, s: str) -> int:
        roman2Int={'I':1,
                   'V':5,
                   'X':10,
                   'L':50,
                   'C':100,
                   'D':500,
                   'M':1000}
        
        N=len(s)
        res=0
        ii=0
        while ii < N:

            if ii+1 < N and roman2Int[s[ii]]<roman2Int[s[ii+1]] :

                res = res+roman2Int[s[ii+1]]-roman2Int[s[ii]]
                ii+=2

            else:
                res += roman2Int[s[ii]]
                ii+=1

        return res
