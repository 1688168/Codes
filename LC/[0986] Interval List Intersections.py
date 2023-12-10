################
# 20231210
################

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

            # no intersection:
            if e1 < s2:
                ii += 1
                continue
            if e2 < s1:
                jj += 1
                continue

            # has intersection

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
                L1[ii][0], L1[ii][1] = e2, e1  # update L1 remaining
            elif e2 > e1:
                ii += 1
                L2[jj][0], L2[jj][1] = e1, e2
            else:
                ii += 1
                jj += 1

        return res

#########################


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # edge cases.
        N1 = len(firstList)
        N2 = len(secondList)
        if N1 == 0 or N2 == 0:
            return []

        firstList.sort()
        secondList.sort()

        i1, i2 = 0, 0
        res = []
        while i1 < N1 and i2 < N2:
            st1, ed1 = firstList[i1]
            st2, ed2 = secondList[i2]

            if st2 > ed1:
                i1 += 1
                continue

            if st1 > ed2:
                i2 += 1
                continue

            ms = max(st1, st2)
            me = min(ed1, ed2)
            res.append([ms, me])

            if ed1 < ed2:
                secondList[i2][0] = ed1
                i1 += 1
            elif ed2 < ed1:
                firstList[i1][0] = ed2
                i2 += 1
            else:
                i1 += 1
                i2 += 1

        return res
