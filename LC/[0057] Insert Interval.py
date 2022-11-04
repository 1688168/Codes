class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        (cs, ce) = newInterval

        res=[]
        for ns, ne in intervals:
            if ne <cs:
                res.append([ns, ne])
            elif ne >= cs and ns <= ce:
                cs=min(cs, ns)
                ce=max(ce, ne)
            elif ns > ce:
                res.append([cs, ce])
                cs, ce = ns, ne
            else:
                print("what's this? ")
        res.append([cs, ce])

        return res
