class Solution {
    public int minDistance(String word1, String word2) {
        int N1=word1.length();
        int N2=word2.length();

        var dp = new int[N1+1][N2+1];
        word1 = "#" + word1;
        word2 = "#" + word2;
        //initialize DP
        for(int ii=0; ii<=N1; ++ii) dp[ii][0]=ii;
        for(int jj=0; jj<=N2; ++jj) dp[0][jj] = jj;

        for(int ii=1; ii<=N1; ++ii){
            for(int jj=1; jj<=N2; ++jj){
                if(word1.charAt(ii)==word2.charAt(jj)){
                    dp[ii][jj] = dp[ii-1][jj-1];
                }else{
                    /**
                        xxxxx //consider update, insert, delete
                        yyyyyyyy
                     */
                    dp[ii][jj] = 1+Math.min(dp[ii-1][jj-1], Math.min(dp[ii][jj-1], dp[ii-1][jj]));
                }

            }
        }

        return dp[N1][N2];
        
    }
}