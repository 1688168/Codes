- Given an Array, find longest increasing subsequence
- dp[ii]: LIS ending @ ii, depends on dp[jj] where jj < ii

### DP: Timeseries type II. single array, dp[ii] depends on dp[jj], nums[jj] where jj < ii

- T: T(N^2)

> DP - bottom up

> Binary Search

1. bisect insert: logN insert for N number -> NlogN
2. dP (Type II): O(N^2)
