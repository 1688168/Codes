class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # if intervals is None
        if intervals is None or len(intervals)==0: return [newInterval]

        # is newInterval ending before first intervals start
        if newInterval[1] < intervals[0][0]: return [newInterval]+intervals

        # is newInterval start after last intervals end
        if newInterval[0] > intervals[-1][1]: return intervals+[newInterval]

        # now we are sure newInterval is somewhere in intervals
        # find the starting point of overlapping
        res=[]
        cs, ce = newInterval
        for ii, (ns, ne) in enumerate(intervals):
            if cs <= ne:
                if ce >= ns:
                    cs, ce = min(cs, ns), max(ce, ne)
                    break
                else:
                    res.append([cs, ce])
                    cs, ce = ns, ne
                    break
        
            res.append([ns, ne])

        for ns, ne in intervals[ii+1:]:
            if ns <= ce:
                cs, ce = min(cs, ns), max(ce, ne)
            else:
                res.append([cs, ce])
                cs, ce = ns, ne
        
        res.append([cs, ce])

        return res

