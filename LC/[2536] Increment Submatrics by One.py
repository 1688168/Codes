class diff2d:
    def __init__(self, m, n):
        # declare a 2d  to record all the queries
        self.m=m
        self.n=n
        self.diff=[[0]*(n+1) for _ in range(m+1)]

        # declare a 2d list for calculated output
        self.out=[[0]*(n+1) for _ in range(m+1)]

    # set method to record query
    def set(self, x0, y0, x1, y1, val):
        self.diff[x0][y0] += val   # we have extra row and extra col to avoid idx out of bound
        self.diff[x0][y1+1] -= val
        self.diff[x1+1][y0] -= val
        self.diff[x1+1][y1+1] += val


    # calc method to compute from diff into out
    def calc(self):
        #self.out[0][0]=self.diff[0][0]
        for ii in range(self.m):
            for jj in range(self.n):
                a=0 if ii==0 else self.out[ii-1][jj]
                b=0 if jj==0 else self.out[ii][jj-1]
                c=0 if (ii==0 or jj==0) else self.out[ii-1][jj-1]                   
                d=self.diff[ii][jj] 
                self.out[ii][jj]=a+b-c+d
    

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        my_2d=diff2d(n, n)
        for q in queries:
            my_2d.set(q[0], q[1], q[2], q[3], 1)
        

        my_2d.calc()
        res=[[0]*n for _ in range(n)]
        for ii in range(n):
            for jj in range(n):
                res[ii][jj]=my_2d.out[ii][jj]
        
        return res


        