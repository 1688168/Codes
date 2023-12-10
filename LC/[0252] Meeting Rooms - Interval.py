
###########################
# 20231210
###########################
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        if len(intervals) == 0:
            return True
        intervals.sort()

        ins, ine = intervals[0]

        for ns, ne in intervals[1:]:
            if ins < ne and ns < ine:
                return False
            else:
                ins, ine = ns, ne

        return True


###########################
# 20231203
###########################

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True
        intervals.sort()
        ins, ine = intervals[0]

        for ns, ne in intervals[1:]:
            if ine <= ns:
                ins, ine = ns, ne
            elif ins < ne and ns < ine:
                return False

        return True


###########################
###########################
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        if len(intervals) == 0:
            return True
        (cs, ce) = intervals[0]

        for ns, ne in intervals[1:]:
            if ns < ce:
                return False
            cs, ce = ns, ne

        return True
