class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        N = len(nums)
        # dp[ii]=max(dp[jj])+nums[ii] where jj in range(max(ii-k, 0), ii)
        # we only care about the max in a sliding window -> sliding window max num pattern
        dq = deque()
        dq.append((nums[0], 0))
        dp=nums[0]
        for ii in range(1, N):
            # evict the oldest
            if dq and ii-dq[0][1] > k: dq.popleft()
           
            dp=dq[0][0]+nums[ii] # calc current dp

            # purge the prior smaller ones
            while dq and dp >= dq[-1][0]: dq.pop()

            dq.append((dp, ii))

        return dp


