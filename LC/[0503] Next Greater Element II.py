class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        0 1 2 0 1
        """
        N=len(nums)
        res=[-1]*N
        stack=[]

        for ii in range(2*N-1):
            """
            01234
            """
            #print("ii: ", ii, "N: ", N, " ii%N: ", ii%N)
            while len(stack)>0 and nums[ii%N] > nums[stack[-1]%N]:
                #print("stack: ", stack)
                res[stack[-1]%N]=nums[ii%N]
                stack.pop()
            #print(" res: ", res)
            stack.append(ii)


        return res
        
