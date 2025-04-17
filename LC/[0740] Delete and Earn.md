> Problem Statements:
* given a single list
* pick any element and delete to earn nums[ii] and also remove all elements with value s.t. value=nums[ii]+/- 1
* N=10^4
* when you delete something -> you cannot take action after -> house robber.

> single array optimize something -> DP I or DP II
* current state: take or skip
* if current state is determined by prev values.  we should be going by value 
* pick any element -> order doesn't matter -> we can sort

> strategy
1. sort the array by list
2. 