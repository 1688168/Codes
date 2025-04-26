//house robber strategy.

class Solution {
    public int minCostII(int[][] costs) {
        int N = costs.length; //num of houses
        int M = costs[0].length;//num of colors
        int[] dp = new int[M]; //min cost ending at house ii with color jj

        //sanity check. no empty house, no empty color
        //initialize dp @ house 0
        for(int jj=0; jj<M; ++jj) dp[jj] = costs[0][jj]; //painting only one house

        for(int ii=1; ii<N; ++ii){//for each house
            int[] tmpDp = dp.clone();//prev state
            for(int jj=0; jj<M; ++jj){//for each color
                dp[jj]=Integer.MAX_VALUE/2;
                for(int kk=0; kk<M; ++kk){
                    if(kk==jj) continue; //no two color in a row
                    dp[jj] = Math.min(dp[jj], tmpDp[kk]+costs[ii][jj]);
                }
            }
        }

        return Arrays.stream(dp) //[java][min][array]
                        .min()
                        .orElseThrow(() -> new RuntimeException("Array is empty"));

    }
}