M=int(1e9)+7
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        """
        => need to know count smaller and bigger
        -> smaller: bisect_left
        -> greater: count_equal
        -> len(nums) so far - less - count_equal
        
        1. instructions: int array
        2. nums: sorted array from instructions
        cost[ii]=min(num_less, num_greater), when inserting iith elements  from instructions into nums
        => sorted nums
        * keep inserting new elements into an sorted array and calc the cost per cost function above
        # bruteforce
        1. binary search for insertion point: logN
        2. shift in order to insert: O(N)

        # divide & conquer: what is the clue?
        - accumulate some statistics (cost based on some cost function, count per some criteria)
        - The statistics has to do with each element's relationship with other elements in the array
        - when dealing with statistics with respect to relations - divide and conquery

        # Divide & Conquer framework:
        - partition the original and merging two sorted list while accumulating the statistids
        - binary search before merging two sorted list
        - operating on two lists: original and sorted
        - merge two sorted list
        """
        idx2smaller=collections.defaultdict(int) #given an index into instructions, record counts that is smaller then the value on the index
     
        def helper(st, ed):
            if st>= ed: return 

            # partition
            mm=st+(ed-st)//2

            # divide
            helper(st, mm)  
            helper(mm+1, ed)

            # conquer
            for ii in range(mm+1, ed+1):#traverse right hand side
                idx = bisect.bisect_left(sorted_instructions, instructions[ii],st, mm+1)
                idx2smaller[ii] += (idx-st)
            
            # merge sorted list
            tmp=[]
            ii=st
            jj=mm+1

            while ii <= mm and jj <= ed:
                if sorted_instructions[ii] <= sorted_instructions[jj]:
                    tmp.append(sorted_instructions[ii])
                    ii+=1
                else:
                    tmp.append(sorted_instructions[jj])
                    jj+=1

            while ii <= mm:
                tmp.append(sorted_instructions[ii])
                ii+=1
            
            while jj <= ed:
                tmp.append(sorted_instructions[jj])
                jj+=1
            
            ii=0
            kk=st
            for ii in range(len(tmp)):
                sorted_instructions[kk]=tmp[ii]
                kk+=1

        N=len(instructions)
        sorted_instructions=instructions[:]
        helper(0, N-1)
        num2cnt=collections.defaultdict(int)#count how many is equal to a given num so far 
        cost=0
        for ii in range(N):
            cost = (cost + min(idx2smaller[ii], 
                              ii-num2cnt[instructions[ii]]-idx2smaller[ii]))%M
            num2cnt[instructions[ii]]+=1
        return cost
        