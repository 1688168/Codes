class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        convert all letters into diff intervals
        merge overlapping intervals
        """
        char2indexes = collections.defaultdict(list)
        N = len(s)
        for ii, cc in enumerate(s):
            char2indexes[cc].append(ii)
        chars = set(list(s))
        intervals = []
        for c in chars:
            intervals.append((char2indexes[c][0], char2indexes[c][-1]))

        intervals.sort(key=lambda x: (x[0], -x[1]))

        cs, ce = intervals[0]

        res = []
        for ns, ne in intervals[1:]:
            if ns < ce:
                cs, ce = min(cs, ns), max(ce, ne)
            else:
                res.append(ce-cs+1)
                cs, ce = ns, ne

        res.append(ce-cs+1)

        return res
