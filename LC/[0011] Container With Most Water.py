class Solution:
    def maxArea(self, height: List[int]) -> int:
        N=len(height)

        ll, rr = 0, N-1
        mxw=0
        while ll < rr:
            w=min(height[ll], height[rr])
            mxw=max(mxw, w*(rr-ll))

            if height[ll] < height[rr]:
                ll+=1
            else:
                rr-=1
        return mxw
            
