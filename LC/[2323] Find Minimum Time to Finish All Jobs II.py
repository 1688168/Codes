#############
# 20240407
#############
class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        """
        jobs[ii]: time for job ii
        workers[ii]: work hour for worker ii
        N=10^5
        => min num of days

        ############
        # bruteforce
        1. N*(N-1)... => return min

        # Greedy heuristic
        """
        jobs.sort()
        workers.sort()
        N = len(jobs)
        required_days = 0
        for ii in range(N):
            required_days = max(required_days, math.ceil(jobs[ii]/workers[ii]))
        return required_days
#############
# 20231007
#############


class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        N = len(workers)
        jobs.sort()
        workers.sort()

        days = [math.ceil(jobs[ii]/workers[ii]) for ii in range(N)]

        return max(days)

####################################


class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort()
        workers.sort()
        N = len(jobs)

        max_days = 0
        for ii in range(N):
            max_days = max(max_days, math.ceil(jobs[ii]/workers[ii]))

        return max_days
