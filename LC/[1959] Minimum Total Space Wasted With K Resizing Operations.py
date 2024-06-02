class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        """
        * N num
        * K resizing
        * dp[ii][jj]: min space wasted @ ii with jj resizing
        """
        N=len(nums)
        
        # declare  dp
        dp=[[math.inf]*(k+1) for _ in range(N)]
        
        # initialize dp
        mx=0
        ttl=0
        for ii in range(N): 
            mx = max(mx, nums[ii])
            ttl += nums[ii]
            dp[ii][0] = mx*(ii+1)-ttl

        for ii in range(1, N): # for each element in nums starting from 1 (0th is initialized above)
            for jj in range(1, min(ii+1, k+1)):
                mx=0
                ttl=0
                for st in reversed(range(1, ii+1)):
                    mx=max(mx, nums[st])
                    ttl += nums[st]
                    dp[ii][jj] = min(dp[ii][jj], dp[st-1][jj-1]+mx*(ii-st+1)-ttl)

        return min(dp[-1])