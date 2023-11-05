class Solution:
    def sortArray(self, nums: List[int]) -> int:
        """
        Observation:
        if nums[0]==0. current swap cnt= k0
        if nums[i] takes ki swaps to be in place.   the required swap cnt that we can only swap with zero is ki+2

        =>
        1. index sort from zero
        2. after zero is in place, regular cnt need to +2 (since we can only swap with zero)
        3. since both [0, 1, 2, ..] and [1, 2, ..., 0] are acceptable answer, we need to try both
        """

        def index_sort(nums):
            N = len(nums)
            ii = 0
            cnt = 0
            while ii < N:
                if nums[ii] == ii:
                    ii += 1
                    continue  # already in place, no swap
                # this part is regular index sort
                while ii < N and nums[ii] != ii and nums[ii] < N and nums[ii] != nums[nums[ii]]:
                    jj = nums[ii]
                    nums[ii], nums[jj] = nums[jj], nums[ii]
                    cnt += 1  # regular index sort count

                if ii > 0:
                    # we can only swap with zero and nums[0] already in place.
                    cnt += 2
                ii += 1

            return cnt

        return min(index_sort(nums[:]), index_sort([nums[-1]]+nums[:-1]))
