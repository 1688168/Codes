class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M=len(matrix)
        N=len(matrix[0])

        top=0
        btm=M
        left=0
        right=N

        res=[]
        while top < btm and left < right:
            #print("top: ", top, " btm: ", btm, " left: ", left, " right: ", right)
            #output top
            for ii in range(left, right):
                res.append(matrix[top][ii])

            top += 1

            #output right
            for ii in range(top, btm):
                res.append(matrix[ii][right-1])

            right -=1

            #check if still valid
            if top == btm or left==right: break

            #output btm
            for ii in reversed(range(left, right)):
                res.append(matrix[btm-1][ii])
            btm -=1

            #output left
            for ii in reversed(range(top, btm)):
                res.append(matrix[ii][left])

            left += 1
        return res
