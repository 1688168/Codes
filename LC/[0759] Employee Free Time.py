###############
# 20231226
###############

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        sweep_line = []
        for sch in schedule:
            for interval in sch:
                sweep_line.append((interval.start, 1))
                sweep_line.append((interval.end, -1))

        sweep_line.sort(key=lambda x: (x[0], -x[1]))

        st = -1
        cnt = 0
        res = []
        for tt, inc in sweep_line:
            cnt += inc

            if cnt == 0 and inc == -1:
                st = tt

            if cnt == 1 and inc == 1 and st != -1:
                res.append(Interval(st, tt))
                st = -1

        return res


####################
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        sweep_line = []
        for sch in schedule:
            for interval in sch:
                sweep_line.append((interval.start, 1))
                sweep_line.append((interval.end, -1))

        # increase first before decrease
        sweep_line.sort(key=lambda x: (x[0], -x[1]))

        res = []
        cnt = 0
        st, ed = -1, -1
        for t, v in sweep_line:
            cnt += v

            if cnt == 0 and v == -1:
                st = t
            elif cnt == 1 and v == 1:
                ed = t
                if st != -1:
                    res.append(Interval(st, ed))
        return res
