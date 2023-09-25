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
