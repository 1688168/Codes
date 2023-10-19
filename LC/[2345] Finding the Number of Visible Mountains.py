class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        """
        Strategy:
        1. convert to invervals O(N)
        2. do we need to sort? Nlog(N)
        3. analyze if any overlap
        Complexity:
        Time: Nlog(N) - sorting
        Space: O(N) - intervals
        """
        cnt = 0
        intervals = [(x-y, x+y) for x, y in peaks]
        intervals.sort()  # intervals always need to sort

        N = len(intervals)
        if N == 1:
            return 1

        cs, ce = -math.inf, -math.inf
        is_dup = False
        for ns, ne in intervals:
            if ns == cs:  # overlapping begin
                if ne > ce:
                    cs, ce = ns, ne
                    cnt += 1
                    is_dup = False

                if ne == ce and not is_dup:  # for duplicates, we can only remove once
                    is_dup = True
                    cnt -= 1
                    cnt = max(cnt, 0)

            else:  # no overlapping on begin
                is_dup = False
                if ne > ce:
                    cnt += 1
                    cs, ce = ns, ne
        return cnt
