"""
# can we go by binary search?
1. can we identify a range
2. is verification helper complexity reasonable?
"""

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        : minimized largest sum of the sub-array
        : binary search on mls (MinimizedLargestSum)
        : if mls is feasible, lower upper-bound (can we go lower)
        : if mls is not feasible, higher the lower-bound
        """
        # determine the search range
        ll=max(nums)
        rr=sum(nums)
        #print(" ll: ", ll, " rr: ", rr)
        mls=float('inf')  # we are looking for the min

        # the helper function
        def is_feasible(mm):
            # if individual element value > mm -> false
            # if requiring more than k groups -> false
            # otherwise return true

            running_sum=0
            cnt=0
            for ii, nn in enumerate(nums): #try partition nums into k groups with max-subarray-sum <= mm
                #print(" cnt: ", cnt, " running sum: ", running_sum, " mm: ", mm)
                if cnt >= k: return False

                if nn > mm: return False # individual element already > mm -> false

                if (running_sum + nn) <= mm: # can I add next value?
                    running_sum += nn
                else:  # one group complete, open new group
                    cnt+=1
                    running_sum=nn
            cnt += 1 # the remainings
            return cnt <= k


        # binary search
        while ll <= rr:
            mm=ll+(rr-ll)//2

            if is_feasible(mm):
                mls=mm
                rr=mm-1
            else:
                ll=mm+1


        return mls
