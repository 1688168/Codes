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