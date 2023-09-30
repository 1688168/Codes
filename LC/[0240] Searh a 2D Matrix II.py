class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        ii = M-1
        jj = 0
        while ii >= 0 and jj < N:
            nn = matrix[ii][jj]
            if nn < target:
                jj += 1
            elif nn == target:
                return True
            else:
                ii -= 1

        return False
