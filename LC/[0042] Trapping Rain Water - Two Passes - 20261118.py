class Solution:
    def trap(self, height: list[int]) -> int:
        N=len(height)
        leftHighest=[0]*N
        rightHighest=[0]*N

        for ii in range(N):
            if ii==0: continue
            leftHighest[ii] = max(height[ii-1], leftHighest[ii-1])
        
        for ii in reversed(range(N)):
            if ii==N-1: continue
            rightHighest[ii] = max(height[ii+1], rightHighest[ii+1])
        
        ans=0
        for ii in range(N):
            if ii==0 or ii==N-1: continue
            ans += max(min(leftHighest[ii], rightHighest[ii])-height[ii], 0)

        return ans

"""
# two pass solution
"""