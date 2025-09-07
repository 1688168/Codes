class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        N=len(arr)
        dp=[1]*N # where dp[ii]=the max jump we can have starting from ii

        sorted_arr = []
        for ii, vv in enumerate(arr):
            sorted_arr.append((vv, ii)) # ascending
        
        sorted_arr.sort()

        for (vv, ii) in sorted_arr: #DP initial state as the highest.
            """
            applying DP strategy, for the current state (the highested), how many next state we can update?
            """

            # update all states that could be reached from current state
            # who can jump from left
            max_so_far = arr[ii]
            for jj in range(ii-1, max(-1, ii-d-1), -1):
                if arr[jj] <= max_so_far: continue
                max_so_far = max(max_so_far, arr[jj])
                dp[jj] = max(dp[jj], dp[ii]+1)

            # jumping right
            max_so_far = arr[ii]
            for jj in range(ii+1, min(N, ii+d+1)):
                if arr[jj] <= max_so_far: continue
                max_so_far = max(max_so_far, arr[jj])
                dp[jj] = max(dp[jj], dp[ii]+1)
            
        return max(dp)
        