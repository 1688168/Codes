class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        N=len(seats)
        emptyRange=[]
        ii=0
        jj=0
        while True:
            while ii<N and seats[ii]==1: ii+=1
            if ii >= N: break
            jj=ii
            while jj<N and seats[jj]==0: jj+=1
            emptyRange.append([ii, jj])
            ii=jj
        mxd=0
        for st, ed in emptyRange:
            if st==0 or ed==N:
                dist=ed-st
                mxd=max(mxd, dist)
            else:
                dist = (ed-st+1)//2
                mxd=max(mxd, dist)
        return mxd