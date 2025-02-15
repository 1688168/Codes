class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int N1 = s1.length();
        int N2 = s2.length();
        if(N1+N2 != s3.length()) return false;
        s1 = '#'+s1;
        s2 = '#'+s2;
        s3 = '#'+s3;

        var dp = new boolean[N1+1][N2+1];
        for(int ii=0; ii<=N1; ++ii){
            for(int jj=0; jj<=N2; ++jj){
                dp[ii][jj]=false;
            }
        }
        /*
            dp[ii][jj]: s1[:ii+1], s2[:jj+1] can interleaving s3[:ii+jj+1]
            dp[ii][jj]: 
        */

        //s1 is null, s2, is null, s3 is also null
        dp[0][0] = true;//earlier we checked s1.length+s2.length=s3.length.

        for(int ii=1; ii<=N1; ++ii){
            dp[ii][0] = dp[ii-1][0] && (s1.charAt(ii)==s3.charAt(ii));
        }

        for(int jj=1; jj<=N2; ++jj){
            dp[0][jj] = dp[0][jj-1] && (s2.charAt(jj)==s3.charAt(jj));
        }

        for(int ii=1; ii<=N1; ++ii){
            for(int jj=1; jj<=N2; ++jj){
                if(s1.charAt(ii)==s3.charAt(ii+jj) && dp[ii-1][jj]){
                    dp[ii][jj]=true;
                }else if(s2.charAt(jj)==s3.charAt(ii+jj) && dp[ii][jj-1]){
                    dp[ii][jj]=true;
                }
            }
        }


 

        return dp[N1][N2];
        
    }
}

/*
Problem statements:
1. s1, s2, s3
2. can you compose S3 by substrings of s1 and s2?
*/