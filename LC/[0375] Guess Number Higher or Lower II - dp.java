/*
* Problem statements:
* given n and a num in [1, n]
* guess a num x, if x==num -> you win
                 else pay x and continue
* you lose if you run out of money before getting the right number
* Analysis:
  O O O O O O O x O O O O O O

  ans = x + max(guess[1, x-1], guess[x+1, n])


*/ 

class Solution {
    public int getMoneyAmount(int n) {
        //dp array
        int[][] dp = new int[n+2][n+2];

        //try all len
        //all starting index
        for(int ll = 2; ll <= n; ++ll){
            for(int ii=1; ii+ll-1<=n; ++ii){
                int jj = ii+ll-1;
                dp[ii][jj]=Integer.MAX_VALUE;
                for(int kk=ii; kk<=jj; ++kk){
                    dp[ii][jj]=Math.min(dp[ii][jj], kk+Math.max(dp[ii][kk-1], dp[kk+1][jj]));
                }
            }
        }

        return dp[1][n];
        
    }
}