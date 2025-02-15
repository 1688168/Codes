# <center><b><span style="color:orange">DP III</span></b></center>

> # <b><span style="color:purple">Pattern</span></b>
* Given two series and asking to optimize something that is in common
* dp[ii][jj]: minimum num of operations required to convert w1[:ii] to w2[:jj]
* dp[ii-1][jj], dp[ii][jj-1], dp[ii-1][jj-1]
* w1[ii]==w2[jj] -> dp[ii][jj]=dp[ii-1][jj-1]
* w1[ii] != w2[jj]
  replace: dp[ii-1][jj-1]+1
  insert a letter to w1: dp[ii][jj-1]+1
  delete a letter from 21: dp[ii-1][jj]+1