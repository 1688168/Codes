class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """
        nums[ii]: int
        => counts[ii]: num of smaller elements to the right of nums[ii]
        
        # bruteforce:
        N=10^4
        for each n scan all elements on the right -> N^2
        
        # divide and conquer
        1. binary search on sorted list: logN
        2. merge sorted list: N
        -> nlogn

        * bisect (binary serch) can identify index that tells you how many are smaller on the left
        * now is asking smaller on the right -> reverse the list
        
        1. reverse the list
        """
        N=len(nums)
        if N==0: return []
        res=[0]*N
        nums=nums[::-1]
        sorted_nums=nums[:]
        # reverse the list
        def helper(st, ed):
            if st >= ed: return # recursion base case
            mm=st+(ed-st)//2
            helper(st, mm)
            helper(mm+1, ed)

            # traverse each right and update the count
            for ii in range(mm+1, ed+1):
                idx = bisect.bisect_left(sorted_nums, nums[ii], st, mm+1)
                res[ii] += (idx-st)

            # merge sorted list
            tmp=[]
            ii=st
            jj=mm+1

            while ii <=mm and jj<= ed:
                if sorted_nums[ii]<=sorted_nums[jj]:
                    tmp.append(sorted_nums[ii])
                    ii+=1
                else:
                    tmp.append(sorted_nums[jj])
                    jj+=1
            
            while ii <= mm:
                tmp.append(sorted_nums[ii])
                ii+=1

            while jj<=ed:
                tmp.append(sorted_nums[jj])
                jj+=1

            
            kk=st
            for ii in range(len(tmp)):
                sorted_nums[kk]=tmp[ii]
                kk+=1

        helper(0, N-1)
        
        # reverse the result
        return res[::-1]