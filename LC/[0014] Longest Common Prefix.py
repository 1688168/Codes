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
