class Solution {
    int M = (int) (Math.pow(10, 9) + 7);
    public int profitableSchemes(int n, int minProfit, int[] group, int[] profit) {
        int N = group.length;
        int[][][] dp = new int[N+1][n+1][minProfit+1];
        List<Integer> group2 = Arrays.stream(group).boxed().collect(Collectors.toList());
        List<Integer> profit2 = Arrays.stream(profit).boxed().collect(Collectors.toList());

        group2.add(0, 0);
        profit2.add(0,0); 
        dp[0][0][0]=1;
        for(int ii=0; ii<N; ++ii){
            for(int jj=0; jj<=n; ++jj){
                for(int kk=0; kk<=minProfit; ++kk){
                    dp[ii+1][jj][kk] = (dp[ii+1][jj][kk] + dp[ii][jj][kk])%M;
                    if(jj+group2.get(ii+1).intValue() <= n){
                        dp[ii+1][jj+group2.get(ii+1).intValue()][(kk+profit2.get(ii+1).intValue() > minProfit?minProfit:kk+profit2.get(ii+1).intValue())] = ( dp[ii+1][jj+group2.get(ii+1).intValue()][(kk+profit2.get(ii+1).intValue() > minProfit?minProfit:kk+profit2.get(ii+1).intValue())] + dp[ii][jj][kk])%M;
                    }
                }
            }
        }
        
        int ans=0;
        for(int jj=0; jj<=n; ++jj){
            ans = (ans + dp[N][jj][minProfit])%M;
        }

        return ans;
    }
}