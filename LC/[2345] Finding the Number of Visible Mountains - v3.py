class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        """

        """
        intervals = [(x-y, x+y) for x, y in peaks]  # convert to intervals
        # interval problems typically you need to sort
        intervals.sort(key=lambda x: (x[0], -x[1]))
        cs, ce = -math.inf, -math.inf

        cnt = 0
        right_most = -1
        N = len(intervals)
        for ii, (ns, ne) in enumerate(intervals):
            if ii > 0 and intervals[ii] == intervals[ii-1]:
                continue
            if ne > right_most:
                right_most = ne
                if ii == N-1 or intervals[ii] != intervals[ii+1]:
                    cnt += 1

        return cnt
