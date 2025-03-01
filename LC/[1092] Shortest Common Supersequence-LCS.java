class Solution {
    public String shortestCommonSupersequence(String str1, String str2) {
        int N1=str1.length();
        int N2=str2.length();

        //setup dummy header to handle edge cases
        String ss = "#" + str1;
        String tt = "#" + str2;

        //declare dp where dp[ii][jj]: lenth of LCS for ss[:ii+1], tt[:jj+1]
        //var dp = new int[N1+1][N2+1];
        //use java stream to declare/initialize all zero 2D array
        var dp = IntStream.range(0, N1+1)
                          .mapToObj(ii -> IntStream.range(0, N2+1)
                                                   .map(jj -> 0).toArray())
                          .toArray(int[][]::new);

        //initialize dp
        //populate dp -> all zero is good

        //LCS strategy: longest common subsequence
        for(int ii=1; ii<=N1; ++ii){
            for(int jj=1; jj<=N2; ++jj){
                if(ss.charAt(ii)==tt.charAt(jj))
                    dp[ii][jj]=dp[ii-1][jj-1]+1;
                else
                    dp[ii][jj] = Math.max(dp[ii-1][jj], dp[ii][jj-1]);
            }
        }
        
        String ret="";
        //backtrack for the path to construct the string
        int ii = N1, jj=N2;
        while(ii>0 && jj>0){
            if(ss.charAt(ii) == tt.charAt(jj)){
                ret = ss.charAt(ii) + ret;
                --ii;
                --jj;
            }else{
                ret = (dp[ii][jj]==dp[ii-1][jj]? ss.charAt(ii--):tt.charAt(jj--)) + ret;
            }
        }
        while(ii>0) ret = ss.charAt(ii--)+ret;
        while(jj>0) ret = tt.charAt(jj--)+ret;

        return ret;
        
    }
}