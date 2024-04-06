class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        N = len(nums)
        cnt = 0
        for ii in range(N):
            lower = 0
            for jj in range(ii):
                if nums[jj] < nums[ii]:
                    lower += 1
            higher = 0
            for kk in range(ii+1, N):
                if nums[kk] < nums[ii]:
                    higher += 1

            if lower >= k and higher >= k:
                cnt += 1

        return cnt
