# <p style="text-align: center"> <span style="color:Orange"> Interval DP</span> </p>
# [`0312`]
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

  
# [`0375`]
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


# [`0516`]
[`problem statement`]
* Given strings -> max palindromic (subsequence) string length  
  
[`analysis`]
* N=1000
> Bruteforce
o o o o o o o


> Greedy  
* would you be able to find a heurictic to partition the string for checking isPalindrom?
  
> DP
* trying to find optimal solution: hint for DP (max length)
* what kind of DP?
* longest increasing subsequence
   

