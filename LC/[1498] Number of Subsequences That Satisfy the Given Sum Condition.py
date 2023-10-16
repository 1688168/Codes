M = int(1e9)+7


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        """
        - this is sortable as we only care about max/min of all subarrays
        - let each ii as the min, the max is the @ jj where min+max <= target
        - nums is power(2, jj-ii)
        - precalc power for performance       
        """
        nums.sort()

        N = len(nums)
        jj = N-1
        ttl = 0
        power = [0]*N
        power[0] = 1
        for ii in range(1, N):
            power[ii] = power[ii-1]*2 % M
        for ii, vv in enumerate(nums):
            while jj >= 0 and nums[jj]+vv > target:
                jj -= 1
            if jj < ii:
                break
            ttl = (ttl+power[jj-ii]) % M

        return ttl
