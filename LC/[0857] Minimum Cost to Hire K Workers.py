class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        qw = sorted(zip(quality, wage), key=lambda x: x[1]/x[0])
        mxq=[]

        acc_q=0
        mnc=float('inf')
        for (q, w) in qw: #higher rate. is always acceptable vs prior lower rate
            rate=w/q

            while len(mxq) > (k-1):
                q_out = -mxq[0]
                heappop(mxq)
                acc_q -= q_out
            
            heappush(mxq, -q)
            acc_q += q
            if len(mxq)==k:
                mnc=min(mnc, acc_q*rate)
                
        return mnc
        