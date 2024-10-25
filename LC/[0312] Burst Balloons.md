> Interval DP  

i x x x x [k] x x x x x j

* what's the last balloon bursted?

* dp[i][j]: max coins you can collect by bursting the balloons[i:j]

* K is the last be bursted
-> dp[i][k-1] + dp[k+1][j] + nums[k]*nums[i-1]*nums[j+1]

> how do you identify this is a interval-DB?
* current profit/loss is associated with (left, right) range
-> dp[i][j]: max coins you can collect by bursting the balloons[i:j]
-> find dp[i][j] by traversing k in (i, j) where k is the last balloon bursted in (i, j) and keep the max