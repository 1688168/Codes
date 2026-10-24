class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        ii = N-1

        while ii >=0:
            if ii==N-1 or nums[ii] >= nums[ii+1]: # skip self, skip if we are still ascending walking backward
                ii-=1
                continue #@ the last digit
            break
        
        # who is the min greater than pivot?
        if ii>=0: # this means we identify pivot, if no pivot, we just reverse order (already the max)
            jj=N-1
            while jj > ii:
                if nums[jj] <= nums[ii]: #strickly ascending (we could have duplicate value)
                    jj-=1
                    continue
                break
            
            # ii is the pivit, jj is the min value before ii
            nums[ii], nums[jj] = nums[jj], nums[ii] #swap with the smallest larger num vs pivot

        # reverse order post ii
        ll, rr = ii+1, N-1
        while ll<rr: 
            nums[ll], nums[rr] = nums[rr], nums[ll]
            ll+=1
            rr-=1
            

        # identify the pivot, and record the min along the way
        # swap the pivot and the min
        # reverse the order


"""
# analysis
> N=100
* 10! > 1M
> try 3 digits. total permutation: 3! -> 3X2X1 -> 6
123 - 
132
213
231
312
321



"""