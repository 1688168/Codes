class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        ii       jj
        2  2  2  3
           i
           j
        """

        ii, jj = 0, len(nums)-1
        while ii <= jj:
            if nums[ii] == val:
                nums[ii]=nums[jj]
                jj -= 1
            else:
                ii+= 1
        
        return ii
        