[`Problem Statement`]  
* given nums and k
* divide nums into k non-empty subarrays
* minimize the largest subarray sum
  
[`Analysis`]  

[`DP`]
* given an array
- ii: 0, N-1
* divide into K partitions
- K: 1, (ii+1)

dp[ii][kk]: min-max-subarray-sum upto index ii of nums and partition into kk subarrays

for each jj in [0, ii]:
dp[ii][kk] = min(dp[ii][kk], 
    max(dp[jj][kk-1], sum[jj+1:ii])
)


* dp[i][k]: nums[0:ii] divide k subarrays, minimized-max_subarray_sum
* dp[i][k]:  max{dp[j][k-1], sum[j+1:i]} over j considering nums[j:i] belongs to the last subarray

x x x x x j x x x x i

N: 1000
i: o, 1, 2, ...
j: 0, 1, 2, i-1
k: 1, 2, 3, ..., i