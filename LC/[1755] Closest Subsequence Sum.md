> Problem statement  
* partition nums (postive/negative num) to two subsets: A (selected), B(skipped)
* given a goal s.t. sum(A) is close to.
* return min abs(sum(A)-goal)

-> whenever being asked to partition a group into two subsets -> origin = A union B
-> Total=sum(A)+sum(B)
-> sum(A)=total-sum(B)
-> goal-sum(A)=goal-total+sum(B)

> can we convert this to a knapsack problem?  
-> cannot do knapsack as resource is positive/negative values)
-> potential goal 2*10^9 -> cannot do knapsack, memory exceed

> neither of above is working (exceeding complexity limit)

> Complexity/pattern analysis
* N<=20
  -> check every subset sum: 2^20

> a use case that we can use kanpsack  
* total |nums| sum <= 1000 (sum of abs(num[ii]))
(ex: 0 <= nums[ii] <= 100)
for x in nums: #for each number
  dp[sum] = dp_old[sum] # skip
  for sum in range(0, 1000+1):#for each capacity/goal
    dp[sum] = dp_old[sum-x] # take

> since N=40, if we partition the nums into A, B (each N1=N2=20)
> We can bruteforce groupA and binary search the complement group B

* subset sums of num1 => sorted (MlogM where m=2^(N/2))
* subset sums of num2 => sorted
-> 2 sum closest

for x in (subset sums of num1) # 2^(N/2)
    find the closest element (goal-x) in (subset sums of nums2) #(log(2^(N/2)))

Time: 2*2^(N/2) + 2^(N/2)*log(2^(N/2))