class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ll, rr, ans = 0, len(nums)-1, -1


        while ll <= rr:
            mm=ll+(rr-ll)//2

            if nums[mm]==target:
                return mm

            if nums[mm] >= nums[0]: # on the left

                if nums[mm] < target or target < nums[0]:
                    ll=mm+1
                else:
                    rr=mm-1


            else: # on the right

                if target < nums[mm] or target >= nums[0]:
                    rr=mm-1
                else:
                    ll=mm+1

        return ans
        
