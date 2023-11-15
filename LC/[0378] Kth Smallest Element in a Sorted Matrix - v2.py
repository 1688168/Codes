class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        M = len(matrix)
        N = len(matrix[0])
        ll, rr, ans = matrix[0][0], matrix[-1][-1], -1

        def count(mm):
            jj = 0
            ii = M-1
            cnt = 0
            while jj < N:
                while ii >= 0:
                    vv = matrix[ii][jj]
                    if vv > mm:
                        ii -= 1
                    else:
                        break
                cnt += (ii+1)
                jj += 1

            return cnt

        while ll <= rr:
            mm = ll+(rr-ll)//2
            if count(mm) < k:
                ll = mm+1
            else:
                ans = mm
                rr = mm-1

        return ans
