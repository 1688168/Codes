class Solution:
    def sortArray(self, nums: List[int]) -> int:
        """
        - for each ii in (0, 1, 2, ...)
        - if nums[ii]==ii: continue (already in the expected place)
        - let the 1st in place index is zero: cnt=something (now nums[0]=0)
        - when ii= 1, 2, ... the index sort will swap with other non-zero index (remember nums[0]=0 already in place)
        - observation (only genius will see this.)  if it takes k swap to have nums[1]=1 (or any non-zero index be in place), the total required swaps (to have zero involved) is k+2
        """

        N = len(nums)

        def index_sort(nums):

            cnt = 0
            ii = 0
            while ii < N:
                # since ii start from zero, 1st place will be zero as the first sorted element
                if nums[ii] == ii:  # if you are alredy in the right place, just skip
                    ii += 1
                    continue

                while ii < N and (nums[ii]) != ii and nums[ii] < N and nums[ii] != nums[nums[ii]]:
                    jj = nums[ii]
                    nums[ii], nums[jj] = nums[jj], nums[ii]
                    cnt += 1  # regular count

                if ii != 0:  # this means 1st place zero is in place, going forward, index sort will only swap with non-zero
                    cnt += 2  # you can only swap with zero.  so the ttl swap cnt = regular swap + 2

                ii += 1

            return cnt

        """
        since [1, 2, 3, 4, 0] and [0, 1, 2, 3, 4] both are acceptable
        this is considered as a circle
        when dealing with -- circle --, we should try min of [1,2,3,4,0] and [0, 1, 2, 3, 4]
        """

        return min(index_sort(nums[:]), index_sort([nums[-1]]+nums[:-1]))


#####################
# This is not working
#####################
class Solution:
    def sortArray(self, nums: List[int]) -> int:
        """
        4 2 0 3 1
        4 0 2 3 1
        4 1 2 3 0
        0 1 2 3 4

        1 2 3 4 0

        1 0 2 4 3
        0 1 2 4 3

        3 1 2 4 0
        3 1 2 0 4
        0 1 2 3 4

        1. index sort until 0 is in beginning or end
        2. scan the list if sorted return
        3. if not sorted, swap 0 with the unsorted and recursion
        """

        N = len(nums)
        cnt = 0

        def index_sort(arr):
            nonlocal cnt
            NN = len(arr)
            ii = 0
            if arr[0] == 0 or arr[-1] == 0:
                return arr
            for ii in range(NN):
                while ii < NN and (arr[ii]) != ii and arr[ii] != arr[arr[ii]]:
                    jj = arr[ii]
                    arr[ii], arr[jj] = arr[jj], arr[ii]
                    cnt += 1
                    # if arr[0]==0 or arr[-1]==0: break
            return arr

        def check_sort(nums):
            is_sorted = True
            for ii in range(N):
                if ii == 0:
                    continue

                if nums[ii] < nums[ii-1]:
                    if ii == N-1 and nums[ii] == 0:
                        break
                    is_sorted = False
                    break
            return is_sorted, ii

        is_sorted = False
        while True and not is_sorted:

            nums = index_sort(nums)

            is_sorted, ii = check_sort(nums)

            if not is_sorted:
                if nums[0] == 0:
                    jj = 0
                    nums[ii], nums[jj] = nums[jj], nums[ii]
                    is_sorted, ii = check_sort(nums)
                    if is_sorted:
                        cnt += 1
                        break

                elif nums[-1] == 0:
                    jj = N-1
                    nums[ii-1], nums[jj] = nums[jj], nums[ii-1]
                    is_sorted, ii = check_sort(nums)
                    if is_sorted:
                        cnt += 1
                        break
                else:
                    nums[ii-1], nums[ii] = nums[ii], nums[ii]
                    cnt += 1

        return cnt
