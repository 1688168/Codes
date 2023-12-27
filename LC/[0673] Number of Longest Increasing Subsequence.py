class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)  # take measument
        dp = [1]*N  # initialize dp
        # recording count of each dp[ii] (initialize to 1)
        idx2cnt = collections.defaultdict(lambda: 1)

        # or we can default this to 1 but traverse ii with range(1, N) << skipping 1
        lis = 0  # default lis to 1

        for ii in range(N):  # for each ii
            for jj in reversed(range(ii)):  # for each jj < ii
                if nums[jj] >= nums[ii]:
                    continue  # ignore those that is violating ""strictly increasing rule"
                if dp[jj]+1 > dp[ii]:  # new LIS @ ii
                    dp[ii] = dp[jj]+1   # new LIS @ ii
                    idx2cnt[ii] = idx2cnt[jj]  # update count
                elif dp[jj]+1 == dp[ii]:
                    # increment count if same LIS @ ii
                    idx2cnt[ii] += idx2cnt[jj]

            lis = max(lis, dp[ii])  # update global LIS

        cnt = 0
        for ii in range(N):
            if dp[ii] == lis:
                cnt += idx2cnt[ii]

        return cnt
