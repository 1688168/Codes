class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        area = [0]*N  # area[ii] is the rectangle area with ii as the heightest
        prev_smaller_equal = [-1]*N
        next_smaller = [N]*N
        stk = []
        for ii, hh in enumerate(heights):
            while len(stk) > 0 and heights[ii] < heights[stk[-1]]:
                hi = stk.pop()
                next_smaller[hi] = ii

            # here we got prev-smaller or equal. this could be a problem
            if len(stk) > 0:
                prev_smaller_equal[ii] = stk[-1]
            stk.append(ii)

        mx = 0
        # print(" next s: ", next_smaller)
        # print(" prev s: ", prev_smaller_equal)
        for ii in range(N):
            mx = max(
                (next_smaller[ii]-prev_smaller_equal[ii]-1)*heights[ii], mx)
        return mx
