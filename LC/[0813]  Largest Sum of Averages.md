> Problem Statements 
* Given nums
* Given k
* Partition nums into k subarrays.
* score = sum of avg of each subarrays
* => max score

> Analysis
* N=100
* k<=N
* Whenever you want to max something
  * greedy
  * search
  * dp
* Whenever you see partition array into K -> type IV DP

> DP IV
* dp[ii][kk]: max score for nums[0:ii+1] with kk partitions
* dp[ii][kk] = max(dp[ii][kk], dp[jj-1][kk-1]+avg(nums[jj:ii])) for jj in [min(kk, jj), ii-1]

