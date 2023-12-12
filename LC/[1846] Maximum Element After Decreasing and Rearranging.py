class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        N=len(arr)
        arr.sort()
        arr[0]=1
        for ii in range(1, N):
            arr[ii]=arr[ii-1]+1 if arr[ii] > arr[ii-1]+1 else arr[ii]
        
        return max(arr)

        
        