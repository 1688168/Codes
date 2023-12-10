class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        N = length
        res = [0]*N

        for st, ed, inc in updates:
            res[st] += inc
            if ed < N-1:
                res[ed+1] -= inc

        for ii in range(1, N):
            res[ii] += res[ii-1]

        return res
