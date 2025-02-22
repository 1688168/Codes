class Solution {
    public String minWindow(String s1, String s2) {
        int N1 = s1.length();
        int N2 = s2.length();

        s1="#"+s1;
        s2="#"+s2;
        //declare dp
        /*
        * dp[ii][jj]: min len of substring s1[:ii+1] s.t. s2[:jj+1] is a subsequence of s1[ii-len+1][ii+1]
        */
        //we want a 2D DP initialized with Integer.MAX_VALUE;
        //var dp = new int[N1+1][N2+1];
        var dp = IntStream.range(0, N1+1)
                          .mapToObj(ii -> IntStream.range(0, N2+1)
                                                   .map(jj -> Integer.MAX_VALUE/2).toArray()
                          ).toArray(int[][]::new);


        //initialize dp
        //s2 len is 0
        for(int ii=1; ii<=N1; ++ii) dp[ii][0] = 0;
        dp[0][0]=0;

        //populate dp
        for(int ii=1; ii<=N1; ++ii){
            for(int jj=1; jj<=N2; ++jj){
                if(s1.charAt(ii)==s2.charAt(jj)){
                    dp[ii][jj] = dp[ii-1][jj-1] + 1;
                }else{
                    dp[ii][jj] = dp[ii-1][jj] + 1;
                }
            }
        }

        String ret="";
        int len=Integer.MAX_VALUE/2;
        int pos = -1;
        for(int ii=1; ii<=N1; ++ii){
            if(dp[ii][N2] < len){
                len=dp[ii][N2];
                pos=ii;
            }
        }

        if(len == Integer.MAX_VALUE/2) return "";
        return s1.substring(pos-len+1, pos+1);
    }
}

/*

*/