#############
# 20240420: code refine
#############
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        """
        ? What's the min time among the workers who spend the max time to complete all jobs?
        * Binary search the min time and see if feasible
        * we are bruteforcing
        """
        # take the size of data
        N = len(jobs)
        NN = 1 << N

        # precalc time
        time = [0]*NN

        for state in range(NN):
            tt = 0
            for ii in range(N):
                if (state >> ii) & 1:
                    tt += jobs[ii]
            time[state] = tt

        ll, rr = 1, sum(jobs)
        ans = math.inf

        def is_feasible(mm, state, kk):  # DFS searching if reachable?
            if state == 0:
                return True  # we finished all jobs without breaching threshold
            if kk >= k:
                return False  # we exceeded ttl workers still haven't finish all jobs
            if (state, kk) in memo:
                return False

            subset = state
            while subset:  # try all subsets
                if time[subset] <= mm:
                    if is_feasible(mm, state-subset, kk+1):
                        return True

                subset = state & (subset-1)

            memo.add((state, kk))
            return False

        while ll <= rr:  # 32
            mm = ll+(rr-ll)//2
            # DFS's best friend
            memo = set()
            if is_feasible(mm, NN-1, 0):
                ans = mm
                rr = mm-1
            else:
                ll = mm+1

        return ans
#############################


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        time = [0]*4096  # time[ii] is the required time to complete state[ii]

        N = len(jobs)

        # precalc time for each state
        for state in range(1 << N):  # 2^N (not including)
            ttl_time = 0
            for ii in range(N):
                if ((state >> ii) & 1) > 0:
                    ttl_time += jobs[ii]

            time[state] = ttl_time

        def is_feasible(state, mm, kk):  # finish the state, with threhold mm, with k workers
            if state == 0:
                return True  # all jobs are finished
            if kk == k:
                return False  # we used more than k workers and still have not reach state zero
            if (state, kk) in memo:
                return False

            subset = state
            # can you find a subset for this worker and finish all recursion for all workers to reach state=0?
            while subset > 0:  # traverse all subsets
                if time[subset] > mm:
                    subset = (subset-1) & state
                    continue  # no worker can exceed the threshold time
                if is_feasible(state-subset, mm, kk+1):
                    return True
                subset = (subset-1) & state

            memo.add((state, kk))
            return False  # there is no way we find a subset under threshold and reaching state=0 for workers under k

        # Binary Search the feasible min max_time
        ll, rr = 1, sum(jobs)
        ans = rr
        while ll <= rr:  # what is the min time of max time of each worker?
            memo = set()
            mm = ll+(rr-ll)//2

            # can you finish all jobs (111111...) with threshold mm from zero workers
            # starting from the worker finish all jobs
            if is_feasible((1 << N)-1, mm, 0):  # can you finish a state given the threshold?
                ans = mm
                rr = mm-1
            else:
                ll = mm+1
        return ans
