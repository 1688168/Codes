class Solution {
    public int maxProfit(int[] prices) {
        int N = prices.length;
        //design a data structure to hold the current state
        //dp[ii][jj] where ii=0, 1, 2 indicate 0, 1, 2 transactions
        //jj = 0, 1 indicate buy(0) or sell(1)
        int dp[][] = new int[3][2]; //use this data structure to carry the status

        //initiazlie dp
        for(int jj=0; jj<=1; ++jj) dp[0][jj] = 0; //no transaction, no profit
        for(int ii=1;ii<3; ++ii) dp[ii][0]=Integer.MIN_VALUE/2;//for 0, 1, 2 transactions and bought 1, the maxProfit 
        for(int ii=1;ii<3; ++ii) dp[ii][1] = 0;
        // dp[0][0] = 0; //no transaction, 

        int mxProfit=0;
        for(int ii=0; ii<N; ++ii){//for each day
            int p = prices[ii];
            for(int jj=2; jj>0; --jj){//going backward to avoid copy states
                //sell transaction
                dp[jj][1] = Math.max(dp[jj][1], dp[jj][0] + p);
                mxProfit = Math.max(mxProfit, dp[jj][1]);
                //buy transaction 
                dp[jj][0] = Math.max(dp[jj][0], dp[jj-1][1]-p);
            }
        }
        return mxProfit;
    }
}