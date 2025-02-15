class Solution {

    public int palindromePartition(String s, int k) {
        int N = s.length();
        s = '#'+s; //java string concatenation

        /*
        * given a string, min edit to make it palindrome
        * dp0[ii][jj]: min edit required to make s[ii:jj+1] palindrome
        * dp0[ii][jj] = dp0[ii+1][jj-1]+ 1 if s[ii]!=s[jj] else 0
        */
        int[][] dp0 = new int[N+1][N+1];
        //single char is always palindrome
        for(int ii=0; ii<=N; ++ii){
            for(int jj=0; jj<=N; ++jj){
                if(ii==jj)
                    dp0[ii][ii]=0;
                else
                    dp0[ii][jj]=jj-ii+1; //or just use Integer.MAX_VALUE/2
            }
        }

        for(int ll=2; ll<=N; ++ll){//for each len
            for(int ii=1; ii+ll-1<=N; ++ii){//for each starting idx of this len
                int jj = ii+ll-1;
                dp0[ii][jj] = dp0[ii+1][jj-1] + (s.charAt(ii)==s.charAt(jj)? 0: 1);
            }
        }

        int[][] dp = new int[N+1][k+1];
        for(int ii=0; ii<=N; ++ii){
            for(int jj=0; jj<=k; ++jj){
                dp[ii][jj] = Integer.MAX_VALUE/2;
            }
        }

        dp[0][0] = 0;

        for(int ii=1; ii<=N; ++ii){
            for(int kk=1; kk <= Math.min(k, ii); ++kk){
                for(int jj=kk; jj<=ii; ++jj){
                    dp[ii][kk] = Math.min(dp[ii][kk], dp[jj-1][kk-1] + dp0[jj][ii]);
                }

            }

        }

        return dp[N][k];
    }
}

/*
Problem statements: given nums and k
    - partition nums in to k non-empty subarrays s.t. each subarray is an palindrome
    - you can change any char whenever necessary
    - the min num of changes you can make all k subarray palindrome

Analysis: 
    - partition array into k sub-array -> DP4
    - dp[ii][kk]: min ops required to make nums[:ii+1] partition into kk subarrays and each subarray is palindrome
    - dp[ii][kk] = min(dp[ii-1][kk-1], x+dp[jj-1][kk-1])
    - where x is the num of ops required to make nums[jj:ii+1] palindrome

> min ops required to make an array palindrome itself is a DP-V
    - dp[ii][jj] = min ops required to make nums[ii:jj+1] palindrome
    - dp[ii][jj] = dp[ii+1][jj-1] + 1 if nums[ii]==nums[jj] else 0


*/