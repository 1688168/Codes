class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        val2MinIdx={}
        val2MaxIdx={}
        N=len(nums)
        max_val=-1
        min_val=pow(10, 5)+1 #math.inf
        for ii, vv in enumerate(nums):
            val2MinIdx[vv]=min(ii, val2MinIdx.get(vv, N))
            val2MaxIdx[vv]=max(ii, val2MaxIdx.get(vv, -1))
            max_val=max(vv, max_val)
            min_val=min(vv, min_val)
        
        num_swap=0
        """
        N=6
        MIdx=3
        swap=N-idx-1
        x x x M x x

        """
        # swap max
        num_swap += (N-val2MaxIdx[max_val]-1)

        # swap min
        # was min moved by max?
        min_idx=val2MinIdx[min_val]
        max_idx=val2MaxIdx[max_val]

        if min_idx > max_idx: min_idx -= 1

        num_swap += min_idx


        return num_swap

        