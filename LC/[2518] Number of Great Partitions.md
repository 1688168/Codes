> Problem statement
1. given a list and an integer k
2. number of ways to partition the list to two lists (A, B), s.t. sum(A) >= k and sum(B) >= k
3. N=1000, k=1000

> Bruteforce:
* T= O(2^1000)


> DP
* single array partition to 2 groups with limitation A
* optimize a single array with limitation -> knapsack
* Partition an Array to two (A, B) is an variation of target sum of a single array

dp[ii][jj]: number of ways sum to jj ending @ ii

* number of ways partitioning array to two (A, B) with sum(A)>=k and sum(B)>=k
  = 2^n of partitions - (num of ways sum(a) < k) * 2 //A and B are symmetric

* Sum(A) >= K and Sum(B) >= K => sum(nums) >= 2k
* sum(A) < K imply sum(B) >= K
* sum(B) < K imply sum(A) >= k 