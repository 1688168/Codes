# https://www.youtube.com/watch?v=GJ-RFWROrv0
class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        jobs.sort()
        workers.sort()
        N = len(jobs)

        max_days = 0
        for ii in range(N):
            max_days = max(max_days, math.ceil(jobs[ii]/workers[ii]))

        return max_days
