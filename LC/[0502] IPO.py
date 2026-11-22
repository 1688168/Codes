class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        capital_profits = sorted(zip(capital, profits))

        cnt=0

        mxq=[]
        ii = 0
        N=len(profits)

        while cnt < k:
            while ii < N and capital_profits[ii][0] <= w:
                heappush(mxq, -capital_profits[ii][1])
                ii+=1
            
            if len(mxq)==0: break
            w += -mxq[0]
            heappop(mxq)

            cnt += 1

        return w