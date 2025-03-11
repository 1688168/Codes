class Solution {
    public int minimumDeleteSum(String s1, String s2) {
        int N1 = s1.length();
        int N2 = s2.length();

        s1 = "#" + s1;
        s2 = "#" + s2;

        var dp = IntStream.range(0, N1+1)
                 .mapToObj(ii -> IntStream.range(0, N2+1)
                                 .map(jj -> Integer.MAX_VALUE/2)
                                 .toArray())
                 .toArray(int[][]::new);
        dp[0][0] = 0;
        for(int ii=1; ii<=N1; ++ii) dp[ii][0] = s1.charAt(ii) + dp[ii-1][0];
        for(int jj=1; jj<=N2; ++jj) dp[0][jj] = s2.charAt(jj) + dp[0][jj-1];

        for(int ii=1; ii<=N1; ++ii){
            for(int jj=1; jj<=N2; ++jj){
                if(s1.charAt(ii)==s2.charAt(jj)){
                    dp[ii][jj] = dp[ii-1][jj-1];
                }else{
                    dp[ii][jj] = Math.min(dp[ii-1][jj]+s1.charAt(ii), dp[ii][jj-1]+s2.charAt(jj));
                }
            }
        }

        return dp[N1][N2];

    }
}
/*
* lowest ASCII sum of deleted chars
* min chars delete to make two strings equal
*/