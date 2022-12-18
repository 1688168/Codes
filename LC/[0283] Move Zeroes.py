class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        0 1 0 3 12
        1 0 0 3 12
        1 3 0 0 12
            i
                j

        1 0
          i
          j
        """
        ii, jj, N = 0, 0, len(nums)

        for jj in range(N):
            if nums[jj] != 0:
                nums[ii], nums[jj]=nums[jj], nums[ii]
                ii+=1


#########################
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        0,1,0,3,12
        i
          j
        """
        ii, jj, N = 0, 0, len(nums)

        while jj < N and ii < N:
            # find first zero per ii
            # find first non-zero per jj
            # swap
            while ii<N and nums[ii] !=0:
                ii +=1

            jj=ii+1
            while jj < N and nums[jj]==0:
                jj+=1

            if jj < N:
                nums[ii], nums[jj] = nums[jj], nums[ii]
