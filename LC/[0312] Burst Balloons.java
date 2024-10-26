class Solution {
    public int maxCoins(int[] iNums) {
      int[] nums = new int[iNums.length + 2]; //java new array; java int array
      int n = 1;
      for (int x : iNums) if (x > 0) nums[n++] = x; //to insert into java array -> clone
      nums[0] = nums[n++] = 1;
  
      int[][] dp = new int[n][n];//java two dimentional array
      for (int k = 2; k < n; ++k)
          for (int left = 0; left < n - k; ++left) {
              int right = left + k;
              for (int i = left + 1; i < right; ++i)
                  dp[left][right] = Math.max(dp[left][right], 
                  nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right]);//java max
          }
  
          return dp[0][n - 1];
      }
  }