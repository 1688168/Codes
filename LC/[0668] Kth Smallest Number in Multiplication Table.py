class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        ll, rr, ans = 1, m*n, -1

        def count(mm):
            ii = m-1
            jj = 0
            cnt = 0
            while jj < n:
                while ii >= 0:
                    vv = (ii+1)*(jj+1)
                    if vv > mm:
                        ii -= 1
                    else:
                        break
                cnt += (ii+1)
                jj += 1
            return cnt

        while ll <= rr:  # 32
            mm = ll+(rr-ll)//2
            if count(mm) < k:
                ll = mm+1
            else:
                ans = mm
                rr = mm-1

        return ans
