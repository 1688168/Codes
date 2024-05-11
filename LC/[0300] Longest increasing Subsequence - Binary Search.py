from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr=[]

        for nn in nums:
            idx=bisect_left(arr, nn)
            if idx >= len(arr):
                arr.append(nn)
            else:
                arr[idx]=nn

        return len(arr)