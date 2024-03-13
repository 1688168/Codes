############
# 20240313
############
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        * intervals 
        * Sorted
        """
        ins, ine = newInterval
        N=len(intervals)

        res=[]
        def has_overlap(a, b):
            a0, a1 = a
            b0, b1 = b
            if b0 > a1: return False
            if a0 > b1: return False
            return True

        for ns, ne in intervals: # for each interval
            if has_overlap((ns, ne), (ins, ine)):# has overlapping with (ins, ine)?
                ins = min(ns, ins)
                ine = max(ne, ine)
            else: # no overlap, who to submit?
                if ine < ns:
                    res.append((ins, ine))
                    ins, ine = ns, ne
                else:
                    res.append((ns, ne))
            
        
        # consider the last one
        res.append((ins, ine))

        return res
        
############
# 20231203
############
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ins, ine = newInterval

        res = []
        for ns, ne in intervals:
            if ine < ns:
                res.append((ins, ine))
                ins, ine = ns, ne
            elif ins <= ne and ns <= ine:
                ins, ine = min(ns, ins), max(ne, ine)
            else:
                res.append((ns, ne))

        res.append((ins, ine))
        return res
############
# 20231030
############


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ins, ine = newInterval

        res = []
        for ns, ne in intervals:
            # inserting interval is before
            if ine < ns:
                res.append((ins, ine))
                ins, ine = ns, ne
            elif ine >= ns and ins <= ne:  # has overlap
                ins = min(ns, ins)
                ine = max(ne, ine)
            else:
                res.append((ns, ne))

        res.append((ins, ine))

        return res


############
# 20230527
############

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        ns, ne = newInterval

        for (cs, ce) in intervals:
            if ns <= ce and ne >= cs:
                ns = min(cs, ns)
                ne = max(ce, ne)
            elif ne < cs:
                res.append([ns, ne])
                ns, ne = cs, ce
            else:
                res.append([cs, ce])
        res.append([ns, ne])

        return res

#################


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        (cs, ce) = newInterval

        res = []
        for ns, ne in intervals:
            if ne < cs:
                res.append([ns, ne])
            elif ne >= cs and ns <= ce:
                cs = min(cs, ns)
                ce = max(ce, ne)
            elif ns > ce:
                res.append([cs, ce])
                cs, ce = ns, ne
            else:
                print("what's this? ")
        res.append([cs, ce])

        return res
