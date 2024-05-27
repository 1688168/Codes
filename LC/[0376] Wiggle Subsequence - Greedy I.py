class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
        # I/O: 
        + nums
        => longest wiggle subsequence of nums

        # Analysis:
        + N=1000
        [Bruteforce:]
        > DFS:
        * 2^1000

        [Greedy I:] 

        """
        N=len(nums)
        if N == 1: return 1

        # remove consecutive equal numbers
        stk=[]

        for nn in nums:
            if not stk or nn != stk[-1]: stk.append(nn)
       
        cnt=2
        nums=stk
        N=len(nums)
        if N <=2: return N
        for ii in range(1, N-1):
            if (nums[ii] > nums[ii-1] and nums[ii] > nums[ii+1]) or (nums[ii] < nums[ii-1] and nums[ii] < nums[ii+1]): cnt+=1


        return cnt