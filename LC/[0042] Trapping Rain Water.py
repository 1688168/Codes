class Solution:
    def trap(self, height: List[int]) -> int:
        N=len(height)
        prev_max=[0]*N
        next_max=[0]*N

        prev=0
        for ii in range(N):
            prev_max[ii]=prev
            prev=max(prev, height[ii])

        prev=0
        for ii in reversed(range(N)):
            next_max[ii]=prev
            prev=max(prev, height[ii])


        ttl=0
        for ii in range(N):
            ttl += max((min(prev_max[ii], next_max[ii])-height[ii]), 0)

        return ttl
