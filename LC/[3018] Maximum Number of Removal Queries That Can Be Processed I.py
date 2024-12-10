class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        N, M = len(nums), len(queries)

        dp = [[0]*N for _ in range(N)]
        #dp[ii][jj]: the max query we can perform for nums in interavl [ii, jj]

        # initialize the DP
        dp[0][N-1] = 0 # we can perform no query when we have full interval (eliminating nothing)

        # DP is moving from known state to unknown state.  since we know intervanl [0, N-1]
        for ll in range(N, 0, -1):  # from full interval to 1
            for ii in range(N-ll+1): # for each interval start. //ii+len-1 <= N-1 -> ii <= ii-len
                jj=ii+ll-1

                # current state from [ii-1, jj]
                if ii-1 >= 0:
                    kk = dp[ii-1][jj]
                    if kk < M and nums[ii-1] >= queries[kk]:
                        dp[ii][jj] = max(dp[ii][jj], 1+dp[ii-1][jj])
                    else:
                        dp[ii][jj] = max(dp[ii][jj], dp[ii-1][jj])

                # current state from [ii, jj+1]
                if jj+1 < N:
                    kk = dp[ii][jj+1]
                    if kk < M and nums[jj+1] >= queries[kk]:
                        dp[ii][jj] = max(dp[ii][jj], 1+dp[ii][jj+1])
                    else:
                        dp[ii][jj] = max(dp[ii][jj], dp[ii][jj+1])

        ans=0

        for ii in range(N):
            kk = dp[ii][ii]
            if kk < M and nums[ii] >= queries[kk]:
                ans = max(ans, 1+kk)
            else:
                ans = max(ans, kk)
            

        return ans