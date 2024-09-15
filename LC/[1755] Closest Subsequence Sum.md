* partition nums to two subsets: A, B
* let sum(A) <= goal <= sum(B)
-> whenever being asked to partition a group into two subsets -> origin = A union B
-> Total=sum(A)+sum(B)
-> sum(A)=total-sum(B)
-> goal-sum(A)=goal-total+sum(B)
=> converting the problem to knapsack problem
* given a list of number
* capacity=goal
* the max total you can choose from the list of number that is <= goal
* return goal-total+sum(B)
-> potential goal 2*10^9 -> cannot do knapsack, memory exceed

> Complexity/pattern analysis
* N<=20
  -> check every subset sum: 2^20

> total |nums| sum <= 1000
(ex: 0 <= nums[ii] <= 100)
for x in nums:
  dp[sum] = dp_old[sum] # skip
  for sum in range(0, 1000):
    dp[sum] = dp_old[sum-x] # take

>> neither of above is working (exceeding complexity limit)

> since N=40, if we partition the nums into A, B (each N1=N2=20)
> We can bruteforce groupA and binary search the complement group B

* subset sums of num1 => sorted (MlogM where m=2^(N/2))
* subset sums of num2 => sorted
-> 2 sum closest

for x in (subset sums of num1) # 2^(N/2)
    find the closest element (goal-x) in (subset sums of nums2) #(log(2^(N/2)))

Time: 2*2^(N/2) + 2^(N/2)*log(2^(N/2))