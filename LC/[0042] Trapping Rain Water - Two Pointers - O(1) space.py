##############
# 20231112
##############
# same idea as two passes but without storage  - O(1) space

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        > Two Pointers        
        """
        N = len(height)
        ll, rr = 0, N-1
        mxl, mxr = 0, 0
        ans = 0
        while ll <= rr:
            mxl = max(mxl, height[ll])
            mxr = max(mxr, height[rr])
            if mxl < mxr:
                ans += (mxl-height[ll])
                ll += 1
            else:
                ans += (mxr-height[rr])
                rr -= 1
        return ans

######################


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        maintain global max-left, max-right: O(1)-space
        process each ii: O(n)-Time
        accumulated water on each ii: ttl+=min(max-left, max-right)
        """
        N = len(height)
        mxl, mxr, acc = 0, 0, 0
        ll, rr = 0, N-1

        while ll <= rr:
            if mxl <= mxr:  # process the lower side
                mxl = max(mxl, height[ll])
                acc += (mxl-height[ll])
                ll += 1
            else:
                mxr = max(mxr, height[rr])
                acc += (mxr-height[rr])
                rr -= 1

        return acc
