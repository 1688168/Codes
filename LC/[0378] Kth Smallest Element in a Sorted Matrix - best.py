class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        M = N = len(matrix)
        ll, rr = int(-1e9), int(1e9)

        ans = -1

        def cnt_smaller_or_equal(mm):
            ii, jj = M-1, 0
            cnt = 0
            while ii >= 0 and jj < N:
                nn = matrix[ii][jj]
                if nn <= mm:
                    cnt += (ii+1)
                    jj += 1
                else:
                    ii -= 1
            # print(" mm: ", mm, " cnt: ", cnt)
            return cnt

        while ll <= rr:
            mm = ll+(rr-ll)//2
            if cnt_smaller_or_equal(mm) < k:
                ll = mm+1
            else:
                ans = mm
                rr = mm-1

        return ans
