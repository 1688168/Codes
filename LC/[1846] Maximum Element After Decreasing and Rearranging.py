############
# 20231225
############
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        N = len(arr)
        for ii in range(1, N):
            if arr[ii] > arr[ii-1]+1:
                arr[ii] = arr[ii-1]+1
        return arr[-1]


##############
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        N = len(arr)
        arr.sort()
        arr[0] = 1
        for ii in range(1, N):
            arr[ii] = arr[ii-1]+1 if arr[ii] > arr[ii-1]+1 else arr[ii]

        return max(arr)
