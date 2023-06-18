class Solution:
    def convert(self, s: str, numRows: int) -> str:
        direction = 1
        N = len(s)
        rr = 0
        s_out = [[] for _ in range(numRows)]
        if numRows == 1:
            return s
        for ii in range(N):
            print(rr)
            s_out[rr].append(s[ii])
            if ii > 0 and ii % (numRows-1) == 0:
                direction *= -1
            rr += direction
        res = ""
        for ii in range(numRows):
            res += "".join(s_out[ii])

        return res
