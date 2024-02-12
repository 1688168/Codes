##############
# 20240212
##############
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        N=len(strs)
        jj=0
        if N==1: return strs[0]

        while True:
            is_common=True
            for ii in range(N-1):
                if jj >= len(strs[ii]) or jj>=len(strs[ii+1]):
                    is_common=False
                    break
                if strs[ii][jj] != strs[ii+1][jj]: 
                    is_common=False
                    break  
            if not is_common:
                ans=jj
                break    
            jj+=1  
    
        res = strs[0][:jj] if jj > 0 else ""
        return res
#################
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        M = len(strs)

        res = ""
        jj = 0
        if len(strs) == 1:
            return strs[0]

        while True:
            for ii in range(1, M):
                if jj >= len(strs[ii]) or jj >= len(strs[ii-1]):
                    return res
                if strs[ii][jj] != strs[ii-1][jj]:
                    return res
            res += strs[0][jj]

            jj += 1

        return res
