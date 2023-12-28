###############
# 20231228
###############
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        1. search + sorted array -> binary search
        2. N < 5k
        3. logN ---> Binary Search
        """
        N = len(nums)
        ll, rr = 0, N-1
        ans = -1

        while ll <= rr:
            mm = ll+(rr-ll)//2

            if nums[mm] == target:
                return mm
            if (nums[mm] < nums[0]) == (target < nums[0]):  # if same side
                if nums[mm] < target:
                    ll = mm+1
                else:
                    rr = mm-1
            else:  # not same side
                if nums[mm] < target:
                    rr = mm-1
                else:
                    ll = mm+1
        return ans

####################


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        ans = -1
        ll, rr = 0, N-1

        while ll <= rr:
            mm = ll+(rr-ll)//2

            if nums[mm] == target:
                return mm  # found, just return
            # this is genius
            #  ---------------------------------------------
            if (nums[mm] >= nums[0]) == (target >= nums[0]):  # mm and target are in the same side
                #  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                if nums[mm] < target:
                    ll = mm+1
                else:
                    rr = mm-1
            elif nums[mm] < target:
                rr = mm-1
            elif nums[mm] > target:
                ll = mm+1
            else:
                raise Exception("Shouldn't see this")

        return ans
