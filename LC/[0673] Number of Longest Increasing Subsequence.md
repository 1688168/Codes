> Given nums -> return number of LIS

### Analysis:
* LIS -> DP
* Additional metrics to collect (additional dictionary)
* dp[ii]: the LIS ending @ ii
* idx2cnt: number of LIS given an index

### Heuristic
* when we have new LIS: count[ii]=count[jj]
* when we found an existing LIS (same LIS but diff subsequence): count[ii] +=1