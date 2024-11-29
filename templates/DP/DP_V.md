# <p style="text-align: center"> <span style="color:Orange"> Interval DP</span> </p>

<p>
  * DP is about how to derive current state from previous state
  * DP[ii]: the value of the DP typically is what the question is asking for (the optimal answer).  cf 3018.  dp[ii][jj]=max query performed.`
  * It will ask you about some optimal solution: max profit/min cost
  * unknow state is derived from previous known state
  * most likely the base case is developing from smaller interval to bigger interval. 
  * but sometimes the know state is the bigger interval and we move from there to smaller interval (3018)
  * You have to review carefully on what is known as starting state and moving bigger or smaller
</p>

<p>
    * Interval DP is always trying to remove something.  On each removal, we create smaller partition.  
    * Interval DP is always from full range and partition into smaller range.
</p>


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

# [`1246`]
[`Problem Statement`]  
* Given a String, remove palindromic substring as one move
* min removal required to remove the string
[`Analysis`]  
* N=20 (bruteforce, greedy, DP)
* DP: 
  * remove something
  * subarray

[`DP type V`]  
* dp[ii][jj]: min removal required to remove substring [ii, jj]
  
* dp[ii][jj] = dp[ii+1][jj-1] if s[ii]=s[jj]
  else
             = 1+min(dp[ii][jj-1], dp[ii+1][jj])
   

   # [`3018`]
   [`Problem Statement`]  
   
    Given:     
     1. nums  
     2. queries
    
    * you can replace the nums with it's subsequence one time @ the beginning  
    => you can remove any elements of nums
  
    * you can eliminate nums[0] or nums[-1] if queries[ii] is >= beginning or ending or nums[ii]  

    Asking => max query num you can perform

[`why this is a DP V`]  
1. N=1000
2. we need to optimize something as result
3. We are removing something and each time we remove something we change the interval size

4. define DP 
dp[ii][jj] = max queries you can perform

5. since we know dp[0][-1]=0  --> we go from max interval and reducing to len=1
6. at end of the date, we will have only one element left. as we cannot possible represent empty interval. so we check all the single char intervals and see if we can eliminate it
7. return the max on those single char use cases.
   




