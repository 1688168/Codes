class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        
        @cache
        def minRemoval(st, ed):
            if st==ed: return 1 # single char is palindrome
            if st+1==ed and arr[st]==arr[ed]: return 1 # repeating char is palindrome
            if st > ed: return 0 # starting index cannot exceed ending index
           
            min_op=math.inf # default to inf for eah range

            for kk in range(st, ed+1): 
                if arr[kk]==arr[ed]: #find a partition point s.t. arr[kk]==arr[ed]
                    min_op = min(min_op, minRemoval(st, kk-1) + max(1, minRemoval(kk+1, ed-1)))
            return min_op
   
        N=len(arr)
        return minRemoval(0, N-1)
        