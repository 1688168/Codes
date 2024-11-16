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

## [20241116 review]

[`312`] VS [`375`]
### 312
* given o o o o x o o o o o
* burst x to collect x*(prev_border)*(next_border) coins
* N=300

[`Bruteforce`]
-> [1, n] -> [1, x-1], [x+1, n] ...
-> n*(n-1)* ...
-> 300!

[`Greedy`]
-> would you be able to come up with a bursting strategy to max the profit?

[`DP`]
-> each time you burst a balloon, we create two sub-intervals
-> can larger interval optimal solution be derived from smaller interavl optimal solution?
-> type V DP (Interval DB)
=> dp[ii][jj]: max profit you can collect in interval [ii, jj]
=> dp[ii][jj] = max(dp[ii][jj], kk+max(dp[ii][kk-1], dp[kk+1, jj]))

  
### 375
* given o o o o o o o x o o o o o o o o o
* guess x if correct game over, else pay x and game continue but you know the guess is too big or too small
* you win if you guess the number correct, you lose if you run out of money before you got the number right

### Analysis
* N:
* each time you guess the number, the original range (interval) is partitioned into two smaller interval
* no good heuristic for applying Greedy
* bruteforce is incrring exponential time-complexity
* interval related DP -> type v DP
=> dp[ii][jj]: min money you need to carry in order to win the game in worst case scenario
=> dp[ii][jj] = min(dp[ii][jj], k+max(dp[ii][kk-1], dp[kk+1][jj]))