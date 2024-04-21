class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        N=len(tasks)
        NN=1<<N #ttl number of states

        ll, rr, ans = 1, N, N # min num of sessions required
        time=[0]*NN

        for state in range(NN):
            ttl=0
            for ii in range(N):
                if (state >> ii) & 1:
                    ttl += tasks[ii]
            
            time[state]=ttl

        def is_feasible(kk, state):
            if state==0: return True
            if kk >= mm: return False
            if (kk, state) in memo: return False
            subset=state
            while subset:
                if time[subset] <= sessionTime and is_feasible(kk+1, state-subset): return True
                subset=state &(subset-1)
            
            memo.add((kk, state))
            return False

        while ll<=rr:
            mm=ll+(rr-ll)//2 # num of sessions required to complete state=111111
            memo=set()
            if is_feasible(0, NN-1):
                ans=mm
                rr=mm-1
            else:
                ll=mm+1

        return ans

        