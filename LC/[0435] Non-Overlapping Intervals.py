########
# 20231224
########
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        when encountering overlap
        remove the one with longer end-time
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))

        ins, ine = -1e5, -1e5
        cnt = 0
        for ns, ne in intervals:
            if ine <= ns:
                ins, ine = ns, ne
                continue
            if ns < ine:  # and ins <= ne:
                cnt += 1
                if ne < ine:  # remove the one ending longer
                    ins, ine = ns, ne  # keep the one ending earlier

        return cnt

        return cnt

########
# 20230527
########


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        (cs, ce) = intervals[0]

        cnt = 0
        for ns, ne in intervals[1:]:
            if ns < ce:
                cnt += 1
                if ne < ce:
                    cs, ce = ns, ne
            else:
                cs, ce = ns, ne

        return cnt


#####################################
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        cs, ce = intervals[0][0], intervals[0][1]
        cnt = 0
        for ns, ne in intervals[1:]:
            if ns < ce:
                cnt += 1
                if ne < ce:
                    cs, ce = ns, ne
            else:
                cs, ce = ns, ne

        return cnt
