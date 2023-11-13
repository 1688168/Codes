class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        1. 3 pass
        2. 1 pass
        """
        N = len(heights)
        stk = []
        prev_smaller = [-1]*N
        next_smaller = [N]*N

        for ii, vv in enumerate(heights):
            while stk and vv < heights[stk[-1]]:
                next_smaller[stk[-1]] = ii
                stk.pop()

            stk.append(ii)
        stk = []
        for ii, vv in enumerate(heights):  # the best way to find prev smaller
            while stk and vv <= heights[stk[-1]]:
                stk.pop()
            if stk:
                prev_smaller[ii] = stk[-1]

            stk.append(ii)

        # print("prev_smaller: ", prev_smaller)
        # print("next_smaller: ", next_smaller)

        mxs = 0
        for ii, vv in enumerate(heights):
            mxs = max(mxs, (next_smaller[ii]-prev_smaller[ii]-1)*heights[ii])

        return mxs
