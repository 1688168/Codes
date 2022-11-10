class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """
        x x x x i
        buy: dp[1] # you need to have something
        dp[i][yes]= max(dp[i-1][no_stock]+buy, dp[i-1][yes]+hold)
        dp[i][no] = max(dp[i-1][has_stock]+sell, dp[i-1][no])


        # this solves buy/sell unlimited time usecase
        N=len(prices)
        for ii in range(N):
            dp[i][yes]= max(dp[i-1][no_stock]+buy, dp[i-1][yes]+hold)
            dp[i][no] = max(dp[i-1][has_stock]+sell, dp[i-1][no])

        # how to limit K times?
        dp[i][yes][j]= max(dp[i-1][no][j-1]+buy, dp[i-1][yes][j]+hold)
        dp[i][no][j]= max(dp[i-1][yes][j]+sell, dp[i-1][no][j]+hold)

        => reduce to two dimentional DP
        hold[i][j]= max(sold[i-1][j-1]+buy, hold[i-1][j])
        sold[i][j]= max(hold[i-1][j]+sell, sold[i-1][j])

        => reduce to two-days-states
        for ii in range(N):
            hold_old, sold_old=hold, sold
            for jj in range(K):
                hold[j]=max(sold_old[j-1]+buy,m hold_old[j])
                sold[j]=max(hold_old[j]+sell, sold_old[j])

        #return max(hold[j], sold[j])
        return sold[j]

        """
        N=len(prices)
        if k >= N//2: # trade k times is 2k days=> unlimited trading usecase
            res=0
            for ii in range(1, N):
                if prices[ii] > prices[ii-1]:
                    res+=prices[ii]-prices[ii-1]
            return res

        hold=[float('-inf')]*(k+1) #hold meaning you have stock after kth transaction
        sold=[float('-inf')]*(k+1) #sold meaning you do NOT have stock after kth transaction
        hold[0]=0
        sold[0]=0

        for ii in range(N): # for all prices (days)
            hold_old, sold_old=hold[:], sold[:]

            # this also works but not really faster
            #  for jj in range(1, min(ii+2, k+1)): # k cannot be bigger than N as that was already handled earlier
            for jj in range(1, k+1): # k cannot be bigger than N as that was already handled earlier
                hold[jj]=max(sold_old[jj-1]-prices[ii],hold_old[jj])
                sold[jj]=max(hold_old[jj]+prices[ii], sold_old[jj])

        ans=float('-inf')
        for n in sold:
            ans=max(n, ans)
        return ans
