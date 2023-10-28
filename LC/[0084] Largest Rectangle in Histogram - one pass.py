############
# 20231028
############
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        heights = [0]+heights+[0]
        mx = 0
        for ii, nh in enumerate(heights):
            while stk and nh < heights[stk[-1]]:
                # next smaller is ii, prev_smaller or equal is in stk[-1]
                curr_ii = stk.pop()
                prev_ii = stk[-1]
                mx = max(heights[curr_ii]*(ii-prev_ii-1), mx)

            stk.append(ii)

        return mx

##########################


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)

        stk = []
        heights = [0] + heights + [0]
        mx = 0
        for ii, hh in enumerate(heights):
            while len(stk) > 0 and heights[ii] < heights[stk[-1]]:
                hi = stk.pop()
                mx = max((ii-stk[-1]-1)*heights[hi], mx)
            stk.append(ii)

        return mx
