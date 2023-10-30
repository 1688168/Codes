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
