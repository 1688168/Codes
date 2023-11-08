##################
# 20231107
##################
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ll, rr = 1, sum(piles)
        ans = -1
        N = len(piles)

        def can_finish(mm):
            tt = 0
            for ii, vv in enumerate(piles):
                tt += math.ceil(vv/mm)

            return True if tt <= h else False

        while ll <= rr:
            mm = ll+(rr-ll)//2
            if can_finish(mm):
                ans = mm
                rr = mm-1
            else:
                ll = mm+1

        return ans


########################
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ll, rr = 1, max(piles)
        ans = -1

        def helper(hr):
            h = 0
            for ii, vv in enumerate(piles):
                h += math.ceil(vv/hr)

            return int(h)

        while ll <= rr:
            mm = ll+(rr-ll)//2
            hrs = helper(mm)
            if hrs > h:
                ll = mm+1
            else:
                ans = mm
                rr = mm-1

        return ans
