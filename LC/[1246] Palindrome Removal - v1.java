class Solution {
    public int minimumMoves(int[] arr) {
        int N = arr.length;
        int[][] dp = new int[N][N];
        for (int ii = 0; ii < N; ++ii) {//here we handled len=1
            dp[ii][ii] = 1; //single char always take one to remove
        }
        for (int len = 2; len <= N; ++len) {//len start from 2. we already taken care of 1 above
            for (int ii = 0; ii < N - len + 1; ++ii) {//for each starting index as ii
                int jj = ii + len - 1;  //define jj 
          
                dp[ii][jj] = Integer.MAX_VALUE;            
                if (arr[ii] == arr[jj]) {
                    // in case length of 2, the min value should be 1
                    dp[ii][jj] = Math.max(dp[ii + 1][jj - 1], 1);
                }
                for (int kk = ii; kk < jj; ++kk) {
                    dp[ii][jj] = Math.min(dp[ii][jj], dp[ii][kk] + dp[kk + 1][jj]);
                }
                
            }
        }
        return dp[0][N - 1];
    }
}