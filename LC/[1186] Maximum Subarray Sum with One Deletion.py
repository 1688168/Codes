class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        """
        # I/O:
        + arr[ii]: int
        => max sum, non-empty subarray

        # Analysis:
        + N=10^5 -> nlogn

        > Bruteforce:
        + take-continue
        + take-start-new
        + no-take

        > DP:

        > Greedy:
        """
        N=len(arr)
        tke_no_delete=-math.inf
        tke_deleted=-math.inf

        mxs=-math.inf
        for ii, nn in enumerate(arr):
            if ii==0:
                tke_no_delete = nn
                tke_deleted=-math.inf
            else:              
                tke_deleted = max(tke_deleted+nn, tke_no_delete) #add current with prev_deleted or delete_current with prev_no_delete
                tke_no_delete = max(nn, tke_no_delete+nn)
            mxs=max(mxs, tke_no_delete, tke_deleted)
        
        return mxs
