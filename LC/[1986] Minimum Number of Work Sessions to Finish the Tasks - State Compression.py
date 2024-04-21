class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        """
        + N=len(tasks)
        + N=14 -> 3^14=4,000,000
        + tasks[ii]: time required for task[ii]
        + 1 worker
        > recognize this is an NP-Hard -> bruteforce
        
        # state compression strategy:
        + state: 111111111111 (14 tasks in ttl, each bit represent 1 task)
        + a subset of state: 11011111111110 meaning if we only have 12 tasks (missing ii=2 and ii=13)
   
        dp[state] = min num of sessions to finish the tasks represented in the state

        dp[state]=dp[subset]+dp[state-subset]
        => dp[11111111111111] << this would be the min # of sessions required to finish all 14 tasks
        """
        N = len(tasks)
        NN=1<<N
        dp=[math.inf]* NN

        # initialize dp - Time: 2^N: this is to identify those states that could be finished in 1 session
        for state in range(NN):
            ttl=0
            for ii in range(N):
                if (state >> ii) & 1: ttl+=tasks[ii]
            
            if ttl <= sessionTime: dp[state]=1
        
        for state in range(NN):
            subset=state
            while subset:
                dp[state] = min(dp[state], dp[subset]+dp[state-subset])
                subset = state & (subset-1)
        

        return dp[-1]