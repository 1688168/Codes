##########
# 20240511
##########

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        1. this is an LIS extension -> asking the number
        2. if we have dp[ii] built where dp[ii] is the LIS @ ii
        3. and dp_cnt where dp_cnt[ii] is the count of LIS ending @ ii
        4. find the global LIS and add all cnt with dp[ii]==global_lis
        """
        nums = [math.inf] + nums
        N=len(nums)

        dp = [1]*N
        dp_cnt = [1]*N

        for ii in range(1, N):
            for jj in reversed(range(1, ii)):
                if nums[jj] >= nums[ii]: continue
                if dp[jj]+1 > dp[ii]:
                    dp_cnt[ii] = dp_cnt[jj]
                elif dp[jj]+1==dp[ii]:
                    dp_cnt[ii] += dp_cnt[jj]
                dp[ii] = max(dp[ii], dp[jj]+1)

        LIS = max(dp)
        cnt=0
        for ii in range(1, N):
            if dp[ii]==LIS: cnt += dp_cnt[ii]
        
        return cnt
##########
# 20240501
##########
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        + nums

        - dp[ii]: LIS ending @ ii
        - dp2[ii]: num of LIS ending @ ii
        """
        N=len(nums)
        idx2cnt=collections.defaultdict(lambda: 1) #record num of LIS ending @ ii
        dp=[1]*N # dp[ii] is the LIS ending @ ii

        LIS=0
        for ii in range(N):
            for jj in reversed(range(ii)):
                if nums[jj] >= nums[ii]: continue # no new LIS
                # here we could have LIS (new or duplicate)
                if dp[jj]+1 > dp[ii]: # we have new LIS
                    dp[ii]=dp[jj]+1
                    idx2cnt[ii]=idx2cnt[jj]
                elif dp[jj]+1==dp[ii]: # we have duplicate LIS
                    idx2cnt[ii]+= idx2cnt[jj]
                
            LIS=max(LIS, dp[ii])
        cnt=0
        for ii in range(N):
            if dp[ii]==LIS: cnt+= idx2cnt[ii]

        return cnt

##########
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
