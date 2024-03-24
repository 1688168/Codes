> Deciding strategy
1. max(N)=12
2. max(K)=12
-> bruteforce

* By past experience, this is a NP question (Job scheduling) -> bruteforce

* Optimize total -> DP



> the time complexity of this "State Compression" DP: 3^N (not 2^N*2^N)

* NP question (expect small N) -> bruteforce
* k<=12: max 12 workers
* jobs <= 12: max 12 jobs
* state=[010101010101]
* eacher worker can take/no-take each job
* each worker can work on: 2^12 states (each job take/no-take)
dp[ii][state]

dp[ii][state]= min(max(dp[ii-1], time(subset))) # over all possible subset of state



Time complexity analysis
state = 1 0
subset of (1,0): 10, 00
subset of (0,1): 01, 00

   



