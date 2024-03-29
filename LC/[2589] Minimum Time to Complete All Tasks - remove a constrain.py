class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        """
        if we remove the condition that 1<=st, ed<=2000
        """
        # for merge overlapping interval -> sort by end
        tasks.sort(key=lambda x: x[1])

        # continue to merge intervals to a new array

        # [st, ed, presum]
        arr=[[-2, -1, 0]] # initialize with a dummy header

        # merging each intervals with duration
        for ii, (st, ed, du) in enumerate(tasks):
            # binary search the insert point
            idx = bisect.bisect_left(arr, [st, 0, 0])
            idx-=1 # dummy header prevents out-of-bound
            
            overlap = arr[-1][2]-arr[idx][2]
            if arr[idx][1] >= st: # has overlap with inserting interval 
                overlap += abs(arr[idx][1]-st)+1
            
            diff = du - overlap
            curr=ed
            while diff > 0:
                gap=abs(arr[-1][1]-curr)
                if diff > gap:
                    diff -= gap
                    curr = arr[-1][0]-1
                    arr.pop()
                else:
                    arr.append([curr-diff+1, ed, arr[-1][2]+ed-(curr-diff)])
                    diff=0
        return arr[-1][-1]
        
#############
class Solution:
    # Nlog(N)
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        # Overlapping interval issue -> sort by end in ascending order
        tasks.sort(key=lambda x: x[1])

        N=len(tasks)

        #arr is of elements: [start, end, presum_runtime]
        arr=[[-2, -1, 0]] #initialized a dummy 
        #Time: N
        for ii, (start, end, duration) in enumerate(tasks): #for each task
            #Time: logN
            idx = bisect.bisect_left(arr, [start, 0, 0])
            #print("idx: ", idx, "ii: ", ii)
            idx -= 1 # the dummy prevents out-of-bound
            if arr[idx][1] < start:#no overlap: prev end < inserting start
                overlap = arr[-1][2]-arr[idx][2] # the time we can run in parallel
            else:# in arr, we only append duration (no non-working hours)
                overlap = arr[-1][2]-arr[idx][2]+abs(arr[idx][1]-start+1)
            diff = duration - overlap #non-parallel times
            curr = end # starting from the tail to fill the gaps
            while diff > 0: #remaining time to fill the gap
                if abs(arr[-1][1]-curr) < diff: #current gap is NOT big enough to host the diff
                    diff -= abs(arr[-1][1]-curr) # fill the current gap
                    curr = arr[-1][0]-1
                    arr.pop()

                else:
                    arr.append([curr-diff+1, end, arr[-1][2]+end-(curr-diff)])
                    diff=0
        return arr[-1][-1]