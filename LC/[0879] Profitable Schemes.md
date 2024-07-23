> Problem statement
* k projects
* profit[ii]=the profit you can get on iith projects
* minProfit
* people[ii]=num of ppl you need on proj ii

-> num of ways to get min profit


> analysis:
* DP:
  a. the number is very big, we have to reduce the complexity
  b. a list of projects and each one you can take or skip
  c. each project has required cost and achievable profit
  d. max profit, min cost, number of ways

* Type I DP: current state @ ii is relating to ii-1 state
  * only need to use tmp var to carry previous state: O(1) space
  * remember to capture prev states in tmp to avoid interfering current state
* Type II DP: current state @ ii is realting to jj's state where jj < ii 
  * this is N^2
* Type III DP: you have two series (two strings)
* Knapsack:
  * a list of resources and each resource has profit/cost
  * there is a constrain on capacity

> 879  
Let dp[ii][jj][kk]: be number of ways on iith project, using jj people and achieving kk profit.

dp[ii][jj][kk] = take+skip
where x=num of ppl required for ii
      y=profit of project ii
      skip=dp[ii-1][jj][kk]
      take=dp[ii-1][jj-x][kk-y]

=> sum(dp[-1][jj][kk]) where kk >=minProfit
Time: 100*100*(100*100) -> 10^8 ---> this will TLE


[`Redesign`]
Let dp[ii][jj][kk]: number of ways on iith proj, using jj people with minProfit=kk

dp[ii][jj][kk] can contribute to  

a: dp[ii+1][jj][kk] += dp[ii][jj][kk]
b: dp[ii+1][jj+people[ii+1]][min(minProfit, kk+profit[ii+1])] += dp[ii][jj][kk]

return sum(dp[-1][ii][minProfit]) where ii is n (max num of people allowed)
