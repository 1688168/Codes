class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        N = len(nums)
        presum = [0]*N

        for ii, vv in enumerate(nums):
            presum[ii] = (presum[ii-1] if ii > 0 else 0) + vv

        cnt = 0
        for ii in range(N):
            for jj in range(ii, N):
                if ii == 0:
                    if presum[jj] == k:
                        cnt += 1
                else:
                    if presum[jj]-presum[ii-1] == k:
                        cnt += 1

        return cnt
