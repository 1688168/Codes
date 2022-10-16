class Solution:
    def countTime(self, time: str) -> int:
        d1=time[0]
        d2=time[1]
        d3=time[3]
        d4=time[4]

        n1=1
        if d1=='?':
            if d2 in ['?', '0', '1', '2', '3']:
                n1=3
            else:
                n1=2
        #print(" d1: ", d1)

        n2=1
        if d2=='?':
            if d1=="?":
                n2=8
            elif d1 in ['0', '1']:
                n2=10
            elif d1=='2':
                n2=4

        n3=1
        if d3=='?':
            n3=6

        n4=1
        if d4=='?':
            n4=10


        return n1*n2*n3*n4
