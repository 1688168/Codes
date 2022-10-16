class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        prev=0
        mxi=0
        mxt=0
        N=len(logs)
        for ii in range(N):
            t=logs[ii][1]-prev
            if t >= mxt:

                if t==mxt:
                    if logs[ii][0] < mxi:
                        mxi=logs[ii][0]
                else:
                    mxi=logs[ii][0]
                    mxt=t

            prev=logs[ii][1]

        return mxi
