class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        """
        1. sort by start: ascending
                   end: decending

        2. initial (st, ed)=(-math.inf, -math.inf)
        3. for each pari, determining who is dominating interval
           - if same as prev -> skip
           - we only need to consider when ne > ce (dominating interval is changing)
           -- if (ns, ne) is last or (ns, ne) != next in line => cnt++

        """
        intervals = [(x-y, x+y) for x, y in peaks]  # convert to intervals

        # this guarantees that intervals with smaller starting time in the front
        # this also guarantees intervals that with same starting time, max ending time in the front
        # interval problems typically you need to sort
        intervals.sort(key=lambda x: (x[0], -x[1]))
        # be careful on make ending point in decending order

        cs, ce = -math.inf, -math.inf
        cnt = 0

        N = len(intervals)
        for ii, (ns, ne) in enumerate(intervals):
            if ii > 0 and intervals[ii] == intervals[ii-1]:
                continue  # skip duplicates, no update on dominating interval
            if ne > ce:  # max ending is sorted in the front.
                # new interval is not covered by current dominating interval
                if ii == N-1 or intervals[ii] != intervals[ii+1]:  # genius
                    cnt += 1  # increment count when you are not duplicating the next interval or you are the last interval

                cs, ce = ns, ne  # updating dominating interval

        return cnt
