class Solution:
    def findMin(self, nums: List[int]) -> int:
        ll, rr, ans = 0, len(nums)-1, -1

        if nums[0] <= nums[-1]:
            return nums[0]



        while ll <= rr:
            mm=ll+(rr-ll)//2

            if nums[mm] >= nums[-1]: # on the left
                ll= mm+1
            else: # on the right
                ans=mm
                rr=mm-1

        return nums[ans]
            
