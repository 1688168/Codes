class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0]*length

        for st, ed, inc in updates:
            for ii in range(st, ed+1):
                res[ii] += inc

        return res
