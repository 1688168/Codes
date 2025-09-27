#######################
# 20250927: use insert template
#######################
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]

        # sort invervals
        #intervals.sort(key=lambda x: (x[0], x[1])) # no need to do this
        intervals.sort()

        # initial interval
        st, ed = intervals[0]

        for ns, ne in intervals[1:]:
            if ns <= ed:
                st=min(st, ns)
                ed=max(ed, ne)
                continue
            res.append([st, ed])
            st, ed = ns, ne
        
        # last interval
        res.append([st, ed])
        return res
        


#######################
# 20231203: use insert template
#######################
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ins, ine = intervals[0]

        res = []
        for ns, ne in intervals:
            if ine < ns:
                res.append((ins, ine))
                ins, ine = ns, ne
            elif ins <= ne and ns <= ine:
                ins, ine = min(ins, ns), max(ine, ne)
            else:
                res.append((ns, ne))

        res.append((ins, ine))

        return res
#######################
#######################


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        cs, ce = intervals[0]

        for ns, ne in intervals[1:]:
            if ns <= ce:
                cs = min(cs, ns)
                ce = max(ce, ne)
            else:
                res.append((cs, ce))
                cs = ns
                ce = ne

        res.append((cs, ce))

        return res
