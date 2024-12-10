class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        
        @cache
        def minRemoval(st, ed):
            if st==ed: return 1 # single char is palindrome
            if st+1==ed and arr[st]==arr[ed]: return 1 # repeating char is palindrome
            if st > ed: return 0 # starting index cannot exceed ending index
           
            min_op=math.inf # default to inf for eah range

            """
            # how do we partition the string and and prune the unnecessary branches?
            1. do we have any opportunity to eliminate two chars in one operation?
               -> try each kk in [ii, jj] and see if we can eliminate both with 1 operation
            2. if we do not have any kk s.t. arr[kk] == arr[jj]
               -> eliminate the jj
            # why we do NOT need to try eleminate ii?
               -> we know nothing works with jj (last char) so remove it, but we do NOT know if any kk could match anything less than jj.  Therefore, keeping jj and removing ii (incur cost 1) cannot possible do better
            """

            for kk in range(st, ed+1): 
                # is there any kk in [ii:jj-1] that can be removed together with jj?, if not, just remove jj and incur cost 1
                # notice the edge case that when len==2 and ii==jj -> base case 1
                if arr[kk]==arr[ed]: #find a partition point s.t. arr[kk]==arr[ed]
                    min_op = min(min_op, minRemoval(st, kk-1) + max(1, minRemoval(kk+1, ed-1)))

                
            return min_op
   
        N=len(arr)
        return minRemoval(0, N-1)
        