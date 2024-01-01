class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        """
        1. convert to intervals
        """
        intervals = [(x-y, x+y) for x, y in peaks]
        intervals.sort(key=lambda x: (x[0], -x[1]))

        ins, ine = math.inf, math.inf
        N = len(intervals)
        cnt = 0
        """
        1.
        --- ---
        2.
        ---
        --

        3. 
        ---
         ---
        """
        # count no overlappings
        duplicates = 0
        is_duplicating = False
        for ns, ne in intervals:
            if ne <= ins:  # indicating first interval
                ins, ine = ns, ne
                continue

            # from here, everything is sorted
            if ine <= ns:  # existing one is independent
                cnt += 1
                ins, ine = ns, ne
                continue

            if ins == ns:  # having same start
                if ine == ne:
                    if not is_duplicating:
                        duplicates += 1
                        is_duplicating = True
                else:
                    is_duplicating = False
                continue  # since we sorted by (x[0], -x[1])
            else:  # not having same start
                if ne <= ine:
                    continue
                elif ne > ine:
                    cnt += 1
                    ins, ine = ns, ne

        return cnt + 1 - duplicates
