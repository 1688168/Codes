class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        K=k+1 # 0, 1, 2, transactions, each transaction has (bought, sold) two states

        dp=[[0]*2 for _ in range(K)]
        dp_tmp=[[0]*2 for _ in range(K)]

        # initialize the state
        dp[0][0]=0 # profit is 0 with 0 transaction bought 
        dp[0][1]=0 # profit is 0 with 0 transaction sold -> we only care about sold

        for ii in range(K):
            dp[ii][0]=-math.inf # all sold state initialize 0 as zero profit

        for ii, pp in enumerate(prices): # for each price
            # copy dp as prev state
            for jj in range(K):
                for kk in range(2):
                    dp_tmp[jj][kk]=dp[jj][kk]

            for kk in range(1, K): # zero transactions will never change anything
                dp[kk][0]=max(dp_tmp[kk][0], dp_tmp[kk-1][1]-pp)
                # no change or bought current after sold prev
                dp[kk][1]=max(dp_tmp[kk][1], dp_tmp[kk][0]+pp)

        mxp=0
        for ii in range(K):
            mxp=max(mxp, dp[ii][1])
        return mxp
     
                