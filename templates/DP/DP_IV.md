# <p style="text-align: center"> <span style="color:Orange">DP Interval I</span> </p>

<p>
* Given an array nums, and partition into K -> optimize something regarding the intervals

* dp[ii][kk]: 
  * iith element
  * KK interval (partition)
  * Search starting index of last interval (jj)
* return dp[N][K]
</p>

# [`0410`]  
[`Problem Statements`]  
* partition nums into k subarrays, find the min max subarray sum

[`Analysis`]
* N=1000

> Bruteforce
* all partitions
- N*(N-1)*... //N!
- sum and find max
- find min of all max
  
[`DP`]
* dp[ii][jj]: min max subarray sum in nums[0:ii+1], kk=jj
* 1000*1000
  

[`Greedy`]
* there is no heuristic on how to partition from localized optimal solution to global optimal solution

[`Binary Search`]
* looking for a min-value s.t. max subarray sum of partitions of nums is less than or equal to the min-value
* guess a value and check if number of required partitions is less than k s.t. each partition sum is less than or equal to the guessed value


# [`0813`]  
[`Problem Statements`] 
[`Analysis`]  
* dp[ii][kk]: the maximized sum of the average of k groups for A[:ii+1]
* [xxxxx][jj xxx ii]
* dp[ii][jj] = max(dp[ii][jj], dp[jj-1][kk-1] + avg[jj:ii+1] for jj=1, 2, ..., ii)