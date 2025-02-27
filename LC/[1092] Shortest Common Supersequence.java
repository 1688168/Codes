class Solution {
    public String shortestCommonSupersequence(String str1, String str2) {
        int N1 = str1.length();
        int N2 = str2.length();

        String s = "#" + str1; //since we need previous state for index 0
        String t = "#" + str2;

        //declare dp
        int[][] dp = new int[N1+1][N2+1]; //consider the dummy header
        /*
        dp[ii][jj]: min len of a ss s.t. s and t are both subsequence of ss
        */

        //initialize dp
        //when ii=0
        for(int jj=1; jj<=N2; ++jj) dp[0][jj] = jj;
        //when jj=0
        for(int ii=0; ii<=N1; ++ii) dp[ii][0] = ii;
        dp[0][0]=0;
        //populate dp
        for(int ii=1; ii<=N1; ++ii){//from 1 due to dummy header
            for(int jj=1; jj<=N2; ++jj){
                if(s.charAt(ii)==t.charAt(jj)){
                    dp[ii][jj] = dp[ii-1][jj-1] +1;
                }else{
                    dp[ii][jj] = Math.min(dp[ii-1][jj], dp[ii][jj-1]) + 1;
                }
            }
        }

        String ret="";
        //backtrack for the path
        int ii = N1;
        int jj = N2;

        while(ii>0 && jj>0){
            if(s.charAt(ii)==t.charAt(jj)){
                ret = s.charAt(ii)+ret;
                --ii;
                --jj;
            }else{
                /*
                xxxxxa
                yyyyb
                zzzzz a
                */
                if(dp[ii][jj]==dp[ii-1][jj]+1){
                    ret = s.charAt(ii--)+ret;
                }else{
                    ret = t.charAt(jj--)+ret;
                }
            }
        }

        while(ii > 0) ret = s.charAt(ii--)+ret; 
        while(jj > 0) ret = t.charAt(jj--)+ret; 
            
        return ret;        
    }
}

/*
Requirement:
* Given s, t two strings, find shortest string ss s.t. s and t are both ss's subsequence
Analysis:
* N: 1000 -> two loops
* two series looking for optimized metrics -> DP III

*/