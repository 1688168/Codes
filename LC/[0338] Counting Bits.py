############
# 20230529
############

class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for ii in range(n+1):
            num=ii
            cnt=0
            while num > 0:
                cnt+= 1
                num &= (num-1)
                print(num)
            res.append(cnt)
        return res



#########################


class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        n     binary   dp[ii]      offset=1
        0     0000     0
        1     0001     1 = 1 + dp[ii-offset]   1 == offset?  no
        2     0010     1+dp[ii-2]2==offset*2=> offset=2
        3     0011     1+dp[ii-2]
        4     0100     4 == offset*2=> offset=4
        5     0101
        6     0110
        7     0111
        8     1000

        """

        offset=1
        dp=[0]*(n+1)

        for ii in range(1,n+1):
            if offset*2==ii: offset*=2
            dp[ii]=1+dp[ii-offset]

        return dp
