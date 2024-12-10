[`Problem Statement`]  
* replacing the array with it's own subsequence meaning we can freely remove any elements of the array whenever we desire

[`Analysis`]  
> Greedy  
* would you be able to come up with an heuristics s.t. we can follow it and achieve the optimal solution? (max queries performed)

> DP
* we are optimizing (max queries) something
* we are removing some elements based on some criteria
* each time we remove something we got a new interval
* Can we try DP V?
  * from smaller interval to big interval (len=1->N)
  * from big interval to small interval (len=N->1)
* dp[ii][jj]: the max queries we can do given range [ii, jj].
```
dfs(0, N-1) = (nums[ii] > query[kk]) + max(dfs(1, N-1), dfs(0, N-2))  
=> we are unable to know what's kk as some subsequence were removed in the beginning
``` 

> how is this DP different from the typical type V DP
* we have an extra dimention to handle -> query and we only know the query status in the beginning 
-> indicating know status is from [0, N-1]
-> deriving status for smaller interval from bigger interval
-> we can try taking kk (the 3rd dimension) into the DFS. but calc the time-complexity.  queries len is also 1K

=> dp[ii][jj]: the maximum number of passed queries when we cut down to [ii:jj]
-> when we have full length (orighnal nums), we cut zero (cannot cut anything)
-> the max num of passed queries will happen when we eliminate all nums (either remove @ beginning or we cut it by query)

Algorithm:
1. use DP from full-length and go down to len=1 see how many queries we can perform. 
2. we cannot go to zero as we need prev/next on ii to leverage the DP
3. all the numbers can either be cut by query or eliminate by initial replacement. so, max queries we can perform definitely will happen when we have no numbers left (worst case scenaro is we could peform zero queries and eliminate all numbers initially)
4. so to determine the optimal answer, we will check if we can eliminate the last number and keep the max.