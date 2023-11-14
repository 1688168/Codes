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
