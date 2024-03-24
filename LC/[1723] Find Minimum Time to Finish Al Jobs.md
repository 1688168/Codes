> Deciding strategy
1. max(N)=12
2. max(K)=12
-> bruteforce

* By past experience, this is a NP question (Job scheduling) -> bruteforce

* Optimize total -> DP


> the time complexity of this "State Compression" DP: 3^N (not 2^N*2^N)

> Analysis
* Since we are bruteforcing this:
  * We need to have all the state of each worker
  * For each worker, s/he could have 2^N diff states where state=[1001011] 
  * Here we use an interger to represent worker[ii] finishes job 0, 3, 5, 6
  * We must compress the state into an integer or we will be easily run out of space
* Given K workers
        N jobs
  each worker has 2^N states (each job take/non-take)
* to represent all states:
  k*2^N (int with state compression)
  - without compression: 
  -> K(workers)*N(jobs)*2(Y/N)
                ^^^^^^^^^^^^^^
                one state (compress as an int)
* dp[ii][state]: min(max(states)) @ worker ii

dp[ii][state]= min(max(dp[ii-1], time(subset))) # over all possible subset of state


> Time complexity analysis
state = 1 0
subset of (1,0): 10, 00
subset of (0,1): 01, 00

> why is python TLE but CPP can AC? or why above strategy is not fast enough?
* above solution tried all possible states, but in fact, some state you don't even need to consider as we are trying to find the min time required to complete all (prune)

* state compression DP is not high performance solution as we solve and find optimal solution. but some state can be pruned in early stage.


> Solution 2: binary search
* low = 1
* high = sum(jobs)
* 

   



