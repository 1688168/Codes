class Solution {
    public int minInsertions(String s) {
        /*
        * -> min insert to make s a palindrome
        * - let s' be the reverse of s
        * - the shortestCommonSuperSubsequence of s and s' is a palindrome
        */
        int N = s.length();
        
        //reverse the string
        String ss = new StringBuilder(s).reverse().toString();

        //prefix dummy 
        s = "#" + s;
        ss = "#" + ss;

        //dp[ii][jj]: SCSS of s and ss
        //define, declare, initialize, populate DP
        var dp = IntStream.range(0, N+1)
                          .mapToObj(ii -> IntStream.range(0, N+1)
                                                   .map(jj -> Integer.MAX_VALUE/2)
                                                   .toArray())
                          .toArray(int[][]::new);
        
        for(int ii = 1; ii<=N; ++ii) dp[ii][0] = ii;
        for(int jj = 1; jj<=N; ++jj) dp[0][jj] = jj;
        dp[0][0] = 0;
   
        for(int ii=1; ii<=N; ++ii){
            for(int jj=1; jj<=N; ++jj){
                if(s.charAt(ii)==ss.charAt(jj)){
                    dp[ii][jj] = dp[ii-1][jj-1] + 1;
                }else{
                    dp[ii][jj] = Math.min(dp[ii-1][jj], dp[ii][jj-1])+1;
                }
            }
        }
 
        //output
        return dp[N][N] - N;
    }
}