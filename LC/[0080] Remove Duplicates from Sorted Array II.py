class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)

        k=0
        two=2
        ll = 0
        """
        k=2

        0 0 1 1 2 3 2 3 3
              l
              i    
            

        k=1
            2
        1 1 1 2 2 3
              l
                i

        """
        for ii in range(N):
            #print(ii, ": ", nums)
            if ii==0:
                ll+=1
                k+=1
            elif nums[ii]==nums[ll-1] and k < two:
                nums[ll]=nums[ii]
                k+=1
                ll+=1       

            elif nums[ii]==nums[ll-1] and k==two:
                continue
            elif k == two:
                nums[ll]=nums[ii]
                k=1
                ll+=1
            else:
                nums[ll]=nums[ii]
                k=1
                ll+=1

        return ll