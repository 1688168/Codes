class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        """
        1. recognize this is an interval question
        => min num of intervals to cover range -> sort by start point
        => max num of intervals of non-overlapping intervals 
        """
        N=n
        # convert to intervals
        intervals=[(ii-ranges[ii], ii+ranges[ii]) for ii in range(n+1)]
        # sort by starting points
        intervals.sort(key=lambda x:[x[0], -x[1]])
        # for each end_point, find max next end_point
        cnt=0 # count of intervals
        far=0 # 0 is the first end_point we identify in scope intervals and find next max end_point
        # ending criteria: end_point is not updating
        # endpoint is not exceeding end of range
        ii=0
        while ii < N:
            cnt +=1
            next_far=far
            while ii <N and intervals[ii][0]<=far:
                next_far=max(next_far, intervals[ii][1])
                ii+=1
            if next_far >= N: return cnt
            if next_far==far: return -1
            far=next_far
     

        return -1