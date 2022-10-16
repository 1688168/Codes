class Solution:
    def findMaxK(self, nums: List[int]) -> int:

        if len(nums)==1: return -1
        nums.sort()


        ll, rr = 0, len(nums)-1

        while ll < rr:
            if abs(nums[rr]) > abs(nums[ll]):
                rr-=1
            elif abs(nums[rr])==abs(nums[ll]):
                break
            else:
                ll+=1

        return nums[rr] if rr > ll and nums[rr] > 0 and (abs(nums[rr]) == abs(nums[ll])) and (nums[rr]+nums[ll]==0) else -1

        
