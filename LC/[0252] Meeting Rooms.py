class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        if len(intervals) ==0: return True
        (cs, ce) = intervals[0]

        for ns, ne in intervals[1:]:
            if ns < ce: return False
            cs, ce = ns, ne


        return True
        
