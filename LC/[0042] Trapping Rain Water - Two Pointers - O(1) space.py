class Solution:
    def trap(self, height: List[int]) -> int:
        """
        : prepare min(left_max, right_max) ->A
        : sum(max(0, A-height)) --> ttl
        : Time: O(N)
        : Space: O(N) <<< can be optimized
        : ---
        : if left is already less than right, only left counts
        """
        N=len(height)
        ll, rr = 0, N-1

        mxl=0
        mxr=0
        acc=0
        while ll < rr:
            if height[ll] <= height[rr]:
                mxl=max(height[ll], mxl)
                acc += mxl-height[ll]
                ll+=1
            else:
                mxr=max(height[rr], mxr)
                acc += mxr-height[rr]
                rr-=1

        return acc
