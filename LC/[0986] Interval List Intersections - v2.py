class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        N1, N2 = len(firstList), len(secondList)
        if N1 == 0 or N2 == 0:
            return []
        L1, L2 = firstList, secondList

        ii, jj = 0, 0

        res = []
        while ii < N1 and jj < N2:
            s1, e1 = L1[ii]
            s2, e2 = L2[jj]

            # taking care of intersections
            if s1 <= e2 and s2 <= e1:
                ins, ine = max(s1, s2), min(e1, e2)
                res.append([ins, ine])
            """
            s1: ------
            s2:    -----
            s2:   ^^^ 
            """

            # figure out the remaining
            if e1 > e2:  # L1 has remaining
                jj += 1  # discared L2 current
            elif e2 > e1:
                ii += 1
            else:
                ii += 1
                jj += 1

        return res
