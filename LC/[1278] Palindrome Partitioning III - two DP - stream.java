class Solution {

    public int palindromePartition(String s, int k) {
        int N = s.length();
        s = '#'+s; //java string concatenation


        //java stream initialize two dimentional array
        int[][] dp0 = IntStream.range(0, N+1) //[0, 1, 2, ..., N]
            .mapToObj(i -> IntStream.range(0, N+1).map(j -> (i == j) ? 0 : j-i+1).toArray())
            .toArray(int[][]::new);


        for(int ii=0; ii<=N; ++ii){
            for(int jj=0; jj<=N; ++jj){
                System.out.println("ii: " + ii + " jj: " + jj + ": "+dp0[ii][jj]);
            }
        }

        for(int ll=2; ll<=N; ++ll){//for each len
            for(int ii=1; ii+ll-1<=N; ++ii){//for each starting idx of this len
                int jj = ii+ll-1;
                dp0[ii][jj] = dp0[ii+1][jj-1] + (s.charAt(ii)==s.charAt(jj)? 0: 1);
            }
        }


        int[][] dp = IntStream.range(0, N+1) //[0, 1, 2, ..., N]
            .mapToObj(i -> IntStream.range(0, N+1).map(j -> Integer.MAX_VALUE/2).toArray())
            .toArray(int[][]::new);

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