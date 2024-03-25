class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        """
        * NP question (expect small N) -> bruteforce
        * k<=12: max 12 workers
        * jobs <= 12: max 12 jobs
        * state=[010101010101]
        * eacher worker can take/no-take each job
        * each worker can work on: 2^12 states (each job take/no-take)
        dp[ii][state]

        dp[ii][state]= min(max(dp[ii-1], time(subset))) # over all possible subset of state
        """

        """
        Time complexity analysis
        state = 1 0
        subset of (1,0): 10, 00
        subset of (0,1): 01, 00
        """
        time=[0]*4096 #time[ii] is the required time to complete state[ii]
        dp=[[math.inf]*4096 for _ in range(14)] # 12+1 rows for initial state, each worker has 4096 states (jobs finished)
        
        N=len(jobs)
        # precalc time for each state
        for state in range(1<<N): #2^N (not including)
            ttl_time=0
            for ii in range(N):
                if ((state>>ii) & 1)>0:
                    ttl_time+=jobs[ii]
            
            time[state]=ttl_time

        # initialize dp[0][x]
        for state in range(1<<N): # for each state 
            dp[0][state]=math.inf
        
        # special initail state: zero worker, zero jobs
        dp[0][0]=0
        
        for ii in range(1,k+1): # k workers given
            for state in range(1<<N): # the inner two loop time is 3^N, (not 2^N*2^N)
                # iterate subset template: https://github.com/wisdompeak/LeetCode/blob/master/Template/Bit_manipulation/Iterate_Subsets.cpp
                # given a state, how to traverse the subset?
                #dp[ii][state]=math.inf
                subset=state
                while subset > 0:
                    dp[ii][state] = min(dp[ii][state], max(dp[ii-1][state-subset], time[subset]))
                                                    #      ^^^ done w/o you ^^^ ^^^ your subset ^^^
                    subset=(subset-1)&state

        
        return dp[k][(1<<N)-1]
            

