class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        memo=set() # dfs's best friend is memo
        time=[0]*4096 #time[ii] is the required time to complete state[ii]
        
        N=len(jobs)

        # precalc time for each state
        for state in range(1<<N): #2^N (not including)
            ttl_time=0
            for ii in range(N):
                if ((state>>ii) & 1)>0:
                    ttl_time+=jobs[ii]
            
            time[state]=ttl_time

        def is_feasible(state, mm, kk):#finish the state, with threhold mm, with k workers
            if state==0: return True # all jobs are finished
            if kk == k: return False # we used more than k workers and still have not reach state zero
            if (state, kk) in memo: return False

            subset=state 
            # can you find a subset for this worker and finish all recursion for all workers to reach state=0?
            while subset > 0: #traverse all subsets
                if time[subset] > mm: 
                    subset = (subset-1)&state
                    continue #no worker can exceed the threshold time
                if is_feasible(state-subset, mm, kk+1): return True
                subset = (subset-1)&state
            
            memo.add((state, kk))
            return False # there is no way we find a subset under threshold and reaching state=0 for workers under k

        # Binary Search the feasible min max_time
        ll, rr = 1, sum(jobs)  
        ans=rr
        while ll<=rr: # what is the min time of max time of each worker?
            memo=set()
            mm=ll+(rr-ll)//2

            # can you finish all jobs (111111...) with threshold mm from zero workers
            # starting from the worker finish all jobs
            if is_feasible((1<<N)-1, mm, 0): #can you finish a state given the threshold?
                ans=mm
                rr=mm-1
            else:
                ll=mm+1
        return ans
            
