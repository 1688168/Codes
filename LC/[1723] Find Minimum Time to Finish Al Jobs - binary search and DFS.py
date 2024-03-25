class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        
        N=len(jobs)
        jobs.sort(reverse=True)#strategy of pruning --- pruning #1
        def is_feasible(workers, mm, kk):#kk is the index into jobs, mm is the threshold each worker can take
            if kk==N: return True
            flag=0
            for ii in range(k):
                # pruning --- 2: reduce to 1/k
                # assigning a job to any new empty worker is the same
                if workers[ii]==0: #assigning a job to an empty worker
                    if flag == 1: continue #to any empty work is same, so no need to search agian with same situation
                    else:
                        flag=1

                if workers[ii]+jobs[kk] > mm: continue
                workers[ii] += jobs[kk]
                if is_feasible(workers, mm, kk+1): return True
                workers[ii]-=jobs[kk]
            return False
    

        # Binary Search the feasible min max_time
        ll, rr = 1, sum(jobs)  
        ans=rr
        while ll<=rr: # what is the min time of max time of each worker?
            
            workers=[0]*k
            mm=ll+(rr-ll)//2

            if is_feasible(workers, mm, 0):  
                ans=mm
                rr=mm-1
            else:
                ll=mm+1    
        return ans
            
