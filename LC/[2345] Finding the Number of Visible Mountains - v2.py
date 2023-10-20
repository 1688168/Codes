###############
# 20231019
###############

class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        """
        1. convert to intervals
        2. sort
        3. evaluate who is the dominate mountain
        """
        intervals = [(x-y, x+y) for x, y in peaks]  # convert to intervals
        intervals.sort()  # interval problems typically you need to sort
        cs, ce = -math.inf, -math.inf
        is_duplicate = False
        cnt = 0
        for ns, ne in intervals:
            if ns == cs:
                if ne > ce:
                    is_duplicate = False
                    cs, ce = ns, ne
                    cnt += 1

                if ce == ne:
                    if not is_duplicate:
                        cnt -= 1
                    is_duplicate = True
            else:
                if ne > ce:
                    is_duplicate = False
                    cs, ce = ns, ne
                    cnt += 1

        return cnt

############################################
############################################


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
        interval2cnt = collections.Counter(intervals)
        # print(" cnts: ", interval2cnt)
        N = len(intervals)
        if N == 1:
            return 1

        cs, ce = -math.inf, -math.inf

        for ns, ne in intervals:
            if ns == cs:  # overlapping begin
                if ne > ce:
                    cs, ce = ns, ne
                    # duplicate intervals cannot participate count
                    if interval2cnt[(ns, ne)] <= 1:
                        cnt += 1

                if ne == ce:  # for duplicates, we can only remove once

                    # duplicate intervals cannot participate count
                    if interval2cnt[(ns, ne)] <= 1:
                        cnt -= 1
                    cnt = max(cnt, 0)

            else:  # no overlapping on begin
                if ne > ce:
                    # duplicate intervals cannot participate count
                    if interval2cnt[(ns, ne)] <= 1:
                        cnt += 1
                    cs, ce = ns, ne
        return cnt
