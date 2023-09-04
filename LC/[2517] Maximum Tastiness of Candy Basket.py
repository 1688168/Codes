"""
https://www.youtube.com/watch?v=ZKeWE8cu_7A
"""


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        ll, rr = 0, pow(10, 9)
        ans = -1

        def isok(mm):
            ii = 0  # must select the first element
            count = 1
            while ii < len(price):
                jj = ii+1
                while jj < len(price) and price[jj]-price[ii] < mm:
                    jj += 1  # find next acceptable price

                if jj >= len(price):
                    return False
                count += 1
                if count >= k:
                    return True
                ii = jj

            return False

        while ll <= rr:
            mm = ll+(rr-ll)//2

            if isok(mm):
                ans = mm
                ll = mm+1
            else:
                rr = mm-1

        return ans
