class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        """
        * N=2000 (2k tasks)
        * [0, 2000]
        """
        N=2001
        time=[0]*N #[0, 1, ..., 2000]
        tasks.sort(key=lambda x: x[1]) #sort by end
        # total runtime (try to overlap as much as you can)
        for ii, (st, ed, duration) in enumerate(tasks): # 2k
            for jj in range(st, ed+1): #2k
                # consume overlap as much as you can
                if time[jj]==1: duration -=1
                if duration ==0: break
            
            jj=ed
            while duration > 0 and jj >=0:
                if time[jj]==0: 
                    time[jj]=1
                    duration -=1
                jj-=1
                # fill gap backward
        return sum(time)

        

########################
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