class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        N = len(nums)
        res = float('inf')
        ll = 0
        ttl = 0
        for rr in range(N):
            ttl += nums[rr]
            if ttl >= target:
                while ll <= rr and ttl >= target:
                    res = min(res, rr-ll+1)
                    ttl -= nums[ll]
                    ll += 1

        return res if res != float('inf') else 0
