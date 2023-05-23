###########
# 20230522
###########
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])

        ll, rr = 0, n-1
        tt, bb = 0, m-1
        res=[]

        while ll <= rr and bb >= tt:          
            # top left to right
            for ii in range(rr-ll+1):              
                res.append(matrix[tt][ll+ii])
            tt += 1

            if tt > bb: break
            # top right to bottom
            for ii in range(bb-tt+1):               
                res.append(matrix[tt+ii][rr])
            rr -= 1

            if rr < ll: break

            # bottom right to left
            for ii in range(rr-ll+1):
                res.append(matrix[bb][rr-ii])
            bb -= 1

            if bb< tt: break

            # bottom left to top
            for ii in range(bb-tt+1):
                res.append(matrix[bb-ii][ll])
            ll += 1
            if ll > rr: break
        
        return res




################################
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
