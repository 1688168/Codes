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
    

    #################################
    # 20231202
    #################################
    class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M=len(matrix)
        N=len(matrix[0])
        ii=M-1
        jj=0
        while ii >=0 and jj < N:
     
            while ii >= 0 and matrix[ii][jj] > target:
                ii-=1
            
            while jj< N and matrix[ii][jj] < target:
                jj+=1
            
            if ii >= 0 and jj < N and matrix[ii][jj]==target: return True
        
        return False
