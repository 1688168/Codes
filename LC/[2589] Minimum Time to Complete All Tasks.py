class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        # sort
        tasks.sort(key=lambda x: x[1])
        time=[0]*2005
        for ii, (a, b, duration) in enumerate(tasks):
            overlap=0
            for t in range(a, b+1):
                if time[t]==1: overlap+=1
            
            if overlap >= duration: continue
            diff = duration-overlap
            for t in range(b, a-1, -1):
                if time[t]==0:
                    time[t]=1
                    diff -= 1
                if diff ==0: break

        return sum(time)