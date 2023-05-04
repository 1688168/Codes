
"""
20230503: T: 5%
"""
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        M=len(mat)    # M rows
        N=len(mat[0]) # N cols

        row=[0]*M
        col=[0]*N

        n2loc = {mat[ii][jj]: (ii, jj) for jj in range(N) for ii in range(M)}
        print(n2loc)
        
        for ii, vv in enumerate(arr):
            rr, cc = n2loc[vv]
            #print(" rr: ", rr, " cc: ", cc)
            row[rr] += 1
            col[cc] += 1
            if row[rr] >= N or col[cc] >= M: return ii
        
        return -1
