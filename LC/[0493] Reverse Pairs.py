class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        """
        => how many pairs s.t. ai > 2aj where i < j
        """
        def helper(st, ed):
            if st >= ed: return 0
            mm=st+(ed-st)//2

            cnt_left=helper(st, mm)
            cnt_right=helper(mm+1, ed)
            cnt=cnt_left+cnt_right

            # process current cnt
            for ii in range(mm+1, ed+1): #for each right

                idx=bisect_right(sorted_num, 2*nums[ii], st, mm+1)
                cnt += (mm-idx+1)
                """
                x x x x x x x
                      ^
                      idx   mm
                """
            
            # inplace merge sorted array
            tmp=[]
            ii=st
            jj=mm+1

            while ii <= mm and jj <= ed:
                if sorted_num[ii] <= sorted_num[jj]:
                    tmp.append(sorted_num[ii])
                    ii+=1
                else:
                    tmp.append(sorted_num[jj])
                    jj+=1
            
            while ii <= mm:
                tmp.append(sorted_num[ii])
                ii+=1
            while jj <= ed:
                tmp.append(sorted_num[jj])
                jj+=1

            ii=0
            kk=st
            while ii < ed-st+1:
                sorted_num[kk]=tmp[ii]
                kk+=1
                ii+=1

            return cnt

        N=len(nums)
        sorted_num=nums[:]
        return helper(0, N-1)

