class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int N1 = text1.length();
        int N2 = text2.length();

        String ss="#"+text1;
        String tt="#"+text2;

        var dp = IntStream
                .range(0, N1+1)
                .mapToObj(ii -> IntStream.range(0, N2+1).map(jj->0).toArray())
                .toArray(int[][]::new);

        for(int ii=1; ii<=N1; ++ii){
            for(int jj=1; jj<=N2; ++jj){
                if(ss.charAt(ii)==tt.charAt(jj)){
                    dp[ii][jj] = dp[ii-1][jj-1] + 1;
                }else{
                    dp[ii][jj] = Math.max(dp[ii-1][jj], dp[ii][jj-1]);
                }
            }
        }

        return dp[N1][N2];
    }
}