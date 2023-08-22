###########
# 20230822
###########
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])

        is_c0_0=False
        
        # traverse all rows
        for ii in range(R):
            # if any of the first column is zero, flag is_c0_0 as True
            if matrix[ii][0]==0: is_c0_0=True
            
            # check all other columns
            for jj in range(1, C):
                if matrix[ii][jj]==0:
                    matrix[0][jj]=0
                    matrix[ii][0]=0
            

        # mark all cells
        for ii in range(1, R):
            for jj in range(1, C):
                if matrix[0][jj]==0 or matrix[ii][0]==0:
                    matrix[ii][jj]=0
        
        if matrix[0][0]==0:
            for ii in range(C):
                matrix[0][ii]=0

        if is_c0_0:
            for ii in range(R):
                matrix[ii][0]=0

            



###################################
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        firstRow=1

        # let row 0, ii indicate if column ii should be zero
        # let row jj col 0 indicate if row jj shouold be zero jj in (1, ...)

        M=len(matrix)
        N=len(matrix[0])

        for ii in range(M):
            for jj in range(N):
                if matrix[ii][jj]==0:
                    # set col:
                    matrix[0][jj]=0

                    # set row:
                    if ii == 0:
                        firstRow=0
                    else:
                        matrix[ii][0] = 0


        for ii in range(1, N):  # set column
            if matrix[0][ii]==0:
                for jj in range(M):
                    matrix[jj][ii]=0

        for ii in range(1, M):
            if matrix[ii][0]==0:
                for jj in range(N):
                    matrix[ii][jj]=0

        if matrix[0][0]==0:
            for jj in range(M):
                matrix[jj][0]=0

        if firstRow==0:
            for jj in range(N):
                matrix[0][jj]=0
