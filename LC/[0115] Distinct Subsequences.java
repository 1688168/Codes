class Solution {
    public int numDistinct(String s, String t) {
        //take size
        int N1 = s.length();
        int N2 = t.length();
      
        s = '#'+s;
        t = '#'+t;

        //declar and define 2D DP
        var dp = IntStream.range(0, N1+1)
                .mapToObj(ii -> IntStream.range(0, N2+1)
                                .map(jj -> 0)
                                .toArray()
                         ).toArray(int[][]::new);
        //initialize the default values
        // - if t is null, all s[ii] can compose null
        for(int ii=0; ii<=N1; ++ii) dp[ii][0] = 1;
        dp[0][0]=1;//null can compose null.  put this at bottom to avoid overlapping

        for(int ii=1; ii<=N1; ++ii){
            for(int jj=1; jj<=N2; ++jj){
                if(s.charAt(ii)==t.charAt(jj)) dp[ii][jj] += dp[ii-1][jj-1];
            
                dp[ii][jj] += dp[ii-1][jj];
            }
        }
 
        return dp[N1][N2];
    }
}