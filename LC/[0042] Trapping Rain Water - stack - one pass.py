class Solution:
    def trap(self, height: List[int]) -> int:
        """
        for each ii: O(N)-Time
        min(prev_greater, next_greater)-height
        """
        N = len(height)
        # prev_greater=[-1]*N
        # next_greater=[N]*N
        stk = []
        ttl = 0
        """
        ii     stk       ttl
        0      [0]       0
        1      [0, 1]    0
        2      

        """
        for ii, vv in enumerate(height):
            # print(" --- ii: ", ii, " stk: ", stk)
            while stk and vv > height[stk[-1]]:
                nxt_greater = vv
                curr = height[stk.pop()]
                prev_greater = 0 if not stk else height[stk[-1]]
                if stk:
                    ttl += max(0, min(prev_greater, nxt_greater) -
                               curr)*(ii-stk[-1]-1)
                # print(" ii: ", ii, " ttl: ", ttl, " next: ", vv, " prev: ", prev_greater, " curr: ", curr, " stk: ", stk)
            stk.append(ii)
        return ttl
