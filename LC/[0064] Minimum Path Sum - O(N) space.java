class Solution {
    public int minPathSum(int[][] grid) {
        //take measurement
        int M=grid.length;
        int N=grid[0].length;

        int[] dp = new int[N];
        //let dp[jj]: min cost reaching grid[ii][jj]
        //where ii is omitted as we only keep status for one row
        //ii=0, jj=0
        dp[0]=grid[0][0];
        //ii=0 (row 0), jj=1...N-1
        for(int jj=1; jj<N; ++jj) dp[jj]=dp[jj-1]+grid[0][jj];

        for(int ii=1; ii<M; ++ii){
            int[] dp2 = new int[N];
            for(int jj=0; jj<N; ++jj){
                if(jj==0) {
                    dp2[jj]=grid[ii][jj]+dp[jj];
                    continue;
                }
                dp2[jj] = Math.min(dp2[jj-1], dp[jj]) + grid[ii][jj];
            }
            dp=Arrays.copyOf(dp2, dp.length);
        }      

        return dp[N-1]; 

    }
}