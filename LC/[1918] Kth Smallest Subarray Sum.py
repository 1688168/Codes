class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        presum = [0]*N

        for ii, vv in enumerate(nums):
            presum[ii] = (presum[ii-1] if ii > 0 else 0) + vv

        ll = min(nums)
        rr = presum[-1]
        ans = -1

        def count(mm):
            cnt = 0

            jj = 0
            for ii, vv in enumerate(presum):
                if presum[ii] <= mm:
                    cnt += (ii+1)
                else:
                    while jj < N and presum[ii]-presum[jj] > mm:
                        jj += 1
                    cnt += (ii-jj)

            return cnt

        while ll <= rr:
            mm = ll+(rr-ll)//2

            if count(mm) < k:
                ll = mm+1
            else:
                ans = mm
                rr = mm-1

        return ans
