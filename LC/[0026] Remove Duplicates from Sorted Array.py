
##############
# 20230605
##############

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        ll=rr=1
        if N == 1: return 1

        """
        1 1 2 
          2 
            l
              r
        """

        while rr < N:
            if nums[rr] != nums[ll-1]:
                nums[ll]=nums[rr]
                ll+=1
            rr += 1
        
        return ll
        


##############
# 20230605
##############

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        ii=1
        """
        1,2,2
          i j

        0 1 2 3 4 2 2 3 3 4
                k
                           i
            j  
        """
        kk=ii=1
        while ii < N: # ii indicate the last unique num we identified so far
            if nums[ii] == nums[kk-1]:
                jj=ii+1
                while jj < N and nums[jj]==nums[kk]:
                    jj+=1
                if jj < N:
                    nums[kk]=nums[jj]                        
                else:
                    break
                
            else:
                nums[kk]=nums[ii]
            while ii < N and nums[ii] <= nums[kk]: ii += 1
            kk += 1
            
        

        return kk