class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        N=len(nums)
        for ii in range(N-1):
            if nums[ii]==nums[ii+1]:
                nums[ii] *= 2
                nums[ii+1]=0

        ii=jj=0
        while jj<N and ii <= jj:
            # find first zero
            while ii < N and nums[ii]!=0:
                ii+=1
            jj=ii
            while jj<N and nums[jj]==0:
                jj+=1

            if jj >= N: break
            nums[ii], nums[jj]=nums[jj], nums[ii]
            ii+=1


        return nums


        
