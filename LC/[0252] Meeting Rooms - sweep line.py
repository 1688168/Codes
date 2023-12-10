class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        sweep line solution
        """
        sweep_line = []
        for st, ed in intervals:
            sweep_line.append((st, 1))
            sweep_line.append((ed, -1))

        sweep_line.sort()
        cnt = 0
        for t, inc in sweep_line:
            cnt += inc
            if cnt > 1:
                return False

        return True
