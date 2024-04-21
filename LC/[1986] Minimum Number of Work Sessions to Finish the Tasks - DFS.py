class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        """
        => Given a sessionTime, => min number of sessions required to group all tasks
        """
        N=len(tasks)
        #sort by reversed order
        tasks.sort(reverse=True)

        ll, rr, ans = 1, N, N

        def is_feasible(st):
            if st==N: return True #all jobs finished with less than K sessions

            flag=False
            for ii in range(mm): #insert jobs in each session see if we can complete
                if flag and sessions[ii]==0: continue
                if sessions[ii]+tasks[st]>sessionTime: continue
                if sessions[ii]==0: flag=True
                sessions[ii] += tasks[st]
                if is_feasible(st+1): return True
                sessions[ii] -= tasks[st] #back track

            return False

        while ll<=rr:
            mm=ll+(rr-ll)//2 #mm is the number of sessions required to complete all tasks
            sessions=[0]*mm #try to assign all tasks to mm sessions all under sessionTime
            
            if is_feasible(0):
                ans = mm
                rr=mm-1
            else:
                ll=mm+1
        return ans