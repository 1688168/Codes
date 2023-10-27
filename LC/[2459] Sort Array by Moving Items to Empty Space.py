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
