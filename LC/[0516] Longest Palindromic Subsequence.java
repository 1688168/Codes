class Solution {
    public int longestPalindromeSubseq(String s) {
      
        int N = s.length();
        s = '#' + s;
          
        var dp = new int[N+1][N+1];
        //initialize the DP
        for(int ii=0; ii<=N; ++ii){
            for(int jj=0; jj<=N; ++jj){
                if(ii==jj) 
                    dp[ii][jj]=1;
                else
                    dp[ii][jj]=0;
            }
        }

        for(int len=2; len<=N; ++len){
            for(int ii=1; ii+len-1 <= N; ++ii){
                int jj=ii+len-1;
                //System.out.println("ii: "+ii+ " jj: "+ jj + " N: " + N + " len: " + len);
                if(s.charAt(ii)==s.charAt(jj)){
                    dp[ii][jj] = Math.max(dp[ii][jj],2+dp[ii+1][jj-1]);
                }else{
                    dp[ii][jj] = Math.max(dp[ii+1][jj], dp[ii][jj-1]);
                }
            }
        }
        return dp[1][N];
    }
}