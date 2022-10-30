class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res=[]
        cs, ce=intervals[0]

        for ns, ne in intervals[1:]:
            if ns <= ce:
                cs=min(cs, ns)
                ce=max(ce, ne)
            else:
                res.append((cs, ce))
                cs=ns
                ce=ne

        res.append((cs, ce))


        return res
        
