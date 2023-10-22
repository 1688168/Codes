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
