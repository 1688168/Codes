##############
# 20240420: code refine
##############
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        N = len(jobs)
        NN = 1 << N

        ll, rr, ans = 1, sum(jobs), math.inf
        # order doesn't matter, have the longest job go first to exceed threshold at early phase
        jobs.sort(reverse=True)

        def is_feasible(mm, jj):
            if jj == N:
                return True  # all job finished

            flag = False
            for ii in range(k):  # which worker can take the job

                if workers[ii]+jobs[jj] > mm:
                    continue

                if flag:
                    continue
                if workers[ii] == 0:
                    flag = True

                workers[ii] += jobs[jj]
                if is_feasible(mm, jj+1):
                    return True
                workers[ii] -= jobs[jj]

            return False

        while ll <= rr:
            mm = ll+(rr-ll)//2
            workers = [0]*k
            if is_feasible(mm, 0):
                ans = mm
                rr = mm-1
            else:
                ll = mm+1

        return ans


#######################
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:

        N = len(jobs)
        jobs.sort(reverse=True)  # strategy of pruning --- pruning #1

        # kk is the index into jobs, mm is the threshold each worker can take
        def is_feasible(workers, mm, kk):
            if kk == N:
                return True  # finished assigning all jobs
            flag = 0
            for ii in range(k):  # which worker we can assign the job to?
                # pruning --- 2: reduce to 1/k
                # assigning a job to any new empty worker is the same
                if workers[ii] == 0:  # assigning a job to an empty worker
                    if flag == 1:
                        continue  # to any empty work is same, so no need to search agian with same situation
                    else:
                        flag = 1

                if workers[ii]+jobs[kk] > mm:
                    continue
                workers[ii] += jobs[kk]
                if is_feasible(workers, mm, kk+1):
                    return True
                workers[ii] -= jobs[kk]  # back track
            return False

        # Binary Search the feasible min max_time
        ll, rr = 1, sum(jobs)
        ans = rr
        while ll <= rr:  # what is the min time of max time of each worker?

            workers = [0]*k
            mm = ll+(rr-ll)//2

            # can you finish assining all jobs to all workers under the threshold?
            if is_feasible(workers, mm, 0):
                ans = mm
                rr = mm-1
            else:
                ll = mm+1
        return ans
