class Solution:
    def search(self, nums: List[int], target: int) -> int:
        while nums and len(nums) > 1 and nums[-1] == nums[0]:
            nums.pop()

        N = len(nums)
        ans = False
        ll, rr = 0, N-1

        while ll <= rr:
            mm = ll+(rr-ll)//2

            if nums[mm] == target:
                return True  # found, just return
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
