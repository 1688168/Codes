class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        N=len(intervals)
        intervals.sort()

        # now we have converted the problem to merge overlapping intervals

        # greedy
        cs, ce = intervals[0]
        res=[]
        for ns, ne in intervals[1:]:
            if ns <= ce:
                cs, ce = cs, max(ce, ne)
            else:
                res.append([cs, ce])
                cs, ce = ns, ne
        
        res.append([cs, ce])

        return res
        

# # Problem
# ## Inputs
# > intervals
# * non-overlapping
# * sorted ascending

# > new interval to insert

# ## Analysis
# * Intervals

# > Greedy
# * convert the insert new interval to merge interval

# > sweepline
# > overlapping intervals are connected -> share same parent -> union find

        