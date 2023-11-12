##############
# 20231112
##############
class Solution:
    def trap(self, height: List[int]) -> int:
        """
        > one pass monotonic stack
        """
        N = len(height)
        stk = []
        ans = 0
        for ii, hh in enumerate(height):
            while stk and hh > height[stk[-1]]:
                curr_ii = stk.pop()
                next_ii = ii
                curr_v = height[curr_ii]
                if stk:
                    dist = (ii-stk[-1]-1)
                    h = min(hh, height[stk[-1]])-curr_v
                    ans += (dist*h)
            stk.append(ii)

        return ans


###############################
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
