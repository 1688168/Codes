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


### Type V DP: Interval
* Optimal solution in big interval can be derived from optimal solution in saller intervals
* for each length in [1, n]
* try each x in [1,n] as the chosen one
* min/max dp[x]

> 312 VS 375

[`312`]
* Given n, pick x in [1, n]
* profit = x * prev * next
* -> max profit
* dp[i][j] = max profit(coins) you can collect by bursting the balloons in [i:j]
  

[`375`]
* Given n, pick x in [1, n]
* cost = x
* -> min cost
* dp[i][j] = min cost (money) you need to prepare to aguaranteed win for the given game on N

