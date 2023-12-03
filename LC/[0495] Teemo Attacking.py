
#################
# 20231203
#################
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        """
        timeSeries: non-decreasing
        """
        ttt = 0
        cs, ce = -1, -1
        for ii, tt in enumerate(timeSeries):  # (ii, tt)=(0,1)
            ns, ne = tt, tt+duration
            if ns <= ce:
                cs, ce = min(cs, ns), max(ce, ne)
            else:
                ttt += (ce-cs)
                cs, ce = ns, ne
            # print(" cs: ", cs, " ce: ", ce, " ttt: ", ttt)

        ttt += (ce-cs)

        return ttt


#################
#################
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        """
        [t, t+duration-1]
        """
        N = len(timeSeries)

        ttt = 0  # total time
        for ii, vv in enumerate(timeSeries):
            if ii+1 < N:
                if vv+duration <= timeSeries[ii+1]:
                    ttt += duration
                else:
                    ttt += (timeSeries[ii+1]-vv)
            else:
                ttt += duration
        return ttt
