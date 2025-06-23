class Solution {
    public int minPathSum(int[][] grid) {
        //take measurement
        int M = grid.length;
        int N = grid[0].length;
        //why DP
        /* current state can be derived from previous state and avoid duplicated calc
        */
        //declare DP
        int[][] dp = new int[M+1][N+1];

        //define DP
        /* dp[ii][jj]: min cost reaching grid[ii][jj]
        * dp[ii][jj] = min(dp[ii-1][jj], dp[ii][jj-1]) + grid[ii][jj]
        */

        //initialize DP
        //ii=0
        for(int jj=0; jj<=N; ++jj){
            dp[0][jj]=Integer.MAX_VALUE;
        }
        //jj=0
        for(int ii=0; ii<=M; ++ii){
            dp[ii][0]=Integer.MAX_VALUE;
        }
        dp[0][0]=0;
        dp[0][1]=0;
        dp[1][0]=0;

        for(int ii=1; ii<=M; ++ii){
            for(int jj=1; jj<=N; ++jj){
                dp[ii][jj] = Math.min(dp[ii-1][jj], dp[ii][jj-1])+grid[ii-1][jj-1];
            }
        }

        // for(int ii=0; ii<=M; ++ii){
        //     for(int jj=0; jj<=N; ++jj){
        //         System.out.print(dp[ii][jj] + ", ");
        //     }
        //     System.out.println();
        // }

        return dp[M][N];
    }
}