class Solution {
    public int minDistance(String word1, String word2) {
        int N1=word1.length();
        int N2=word2.length();
        String ss = "#"+word1;
        String tt = "#"+word2;

        //declare dp
        var dp = IntStream.range(0, N1+1)
                 .mapToObj(ii->IntStream.range(0, N2+1)
                               .map(jj->Integer.MAX_VALUE/2)
                               .toArray()
                          ).toArray(int[][]::new);
        ;

        //initialize dp
        //if ss is null
        for(int jj=1; jj<=N2; ++jj) dp[0][jj]=jj;
        //if tt is null
        for(int ii=1; ii<=N1; ++ii) dp[ii][0]=ii;

        dp[0][0]=0;

        //populate dp
        for(int ii=1; ii<=N1; ++ii){
            for(int jj=1; jj<=N2; ++jj){
                if(ss.charAt(ii)==tt.charAt(jj)){
                    dp[ii][jj] = Math.min(dp[ii][jj], dp[ii-1][jj-1]);
                }else{
                    dp[ii][jj] = Math.min(dp[ii][jj], Math.min(dp[ii-1][jj], dp[ii][jj-1])+1);
                }
            }
        }

        return dp[N1][N2];
    }
}