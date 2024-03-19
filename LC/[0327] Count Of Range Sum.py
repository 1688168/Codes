class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        """
        N=10^5
        => number of range sums in [lower, upper]
        sum[ii:jj] in [lower, upper]
        lower <= presum[jj]-presum[ii-1] <= upper
        presum[ii-1] <= presum[jj]-lower
        presum[ii-1] >= presum[jj]-upper

        * presum itself is like nums (just an int list)
        -> find number of pairs that satisfy the constrain above
        -> count pairs of some condition -> "divide and conquer"
        """
        presum=[0]
        for n in nums:
            presum.append(presum[-1]+n)
        N=len(presum)

        def divide_and_conquer(st, ed):
            if st>=ed: return 0
            ret=0
            mm=st+(ed-st)//2
            ret += divide_and_conquer(st, mm)
            ret += divide_and_conquer(mm+1, ed)

            """
            A: [X X X X X] B: [Y Y Y Y Y Y]
                                 ^.    ^
            for each Ai
            how many pairs of [x, y] that falls in range?
            """
            for ii in range(st, mm+1): # search each left
                li = bisect_left(presum, presum[ii]+lower, mm+1, ed+1)
                ui = bisect_right(presum, presum[ii]+upper, mm+1, ed+1)
                ret += (ui-li)
            tmp=[]
            ii=st
            jj=mm+1

            while ii <= mm and jj <= ed:
                if presum[ii] <= presum[jj]:
                    tmp.append(presum[ii])
                    ii+=1
                else:
                    tmp.append(presum[jj])
                    jj+=1
            
            while ii<=mm:
                tmp.append(presum[ii])
                ii+=1
            
            while jj<=ed:
                tmp.append(presum[jj])
                jj+=1

            kk=st
            for ii in range(len(tmp)):
                presum[kk]=tmp[ii]
                kk+=1
            return ret        

        return divide_and_conquer(0, N-1)

        