class Solution:
    def trap(self, height: List[int]) -> int:
        h = height
        N = len(height)
        prev_max = [0]*N
        next_max = [0]*N
        prev_max[0] = h[0]
        next_max[-1] = h[-1]
        for ii in range(1, N):
            prev_max[ii] = max(prev_max[ii-1], h[ii])
            next_max[N-1-ii] = max(next_max[N-1-ii+1], h[N-1-ii])

        acc = 0
        for ii in range(N):
            acc += max(min(prev_max[ii], next_max[ii])-h[ii], 0)

        return acc


############
# 20230616
############
"""
Pass I:
1. record prev max and next max
2. for each ii, water = min(prev_max, next_max)-curr_height
Pass II:
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)

        left_max = [0]*N
        right_max = [0]*N
        water = [0]*N
        for ii in range(1, N):
            left_max[ii] = max(left_max[ii-1], height[ii-1])
            right_max[N-1-ii] = max(right_max[N-ii], height[N-ii])

        # print("left: ", left_max)
        # print("right: ", right_max)

        for ii in range(N):
            water[ii] = max(0, min(left_max[ii], right_max[ii])-height[ii])

        return sum(water)

##########################


class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        prev_max = [0]*N
        next_max = [0]*N

        prev = 0
        for ii in range(N):
            prev_max[ii] = prev
            prev = max(prev, height[ii])

        prev = 0
        for ii in reversed(range(N)):
            next_max[ii] = prev
            prev = max(prev, height[ii])

        ttl = 0
        for ii in range(N):
            ttl += max((min(prev_max[ii], next_max[ii])-height[ii]), 0)

        return ttl
