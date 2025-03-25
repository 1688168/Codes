# <center><b><span style="color:orange">123</span></b></center>

> ### <b><span style="color:green">Analysis</span></b>

1. single array, N=10^5
2. base case:
   * initial states: [-inf, -inf, -inf, -inf] (since we are trying to find max profit)
3. current states:
    * b1, s1, b2, s2
    * we can represent the states with 4 variables: b1, s1, b2, s2
    * or we can represent the states in an 2D array dp[3][2]
    where 3 represent 0, 1, 2 transactions
          2 represent 0: bought, 1, sold

4. required previous states
   * only need previous state
  
> ### <b><span style="color:green">Implementations</span></b>
1. bruteforce (DFS)
2. 4 var states
3. array states

  