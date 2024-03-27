class Solution:
    # Nlog(N)
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        # Overlapping interval issue -> sort by end
        tasks.sort(key=lambda x: x[1])

        N=len(tasks)

        #arr is of elements: [start, end, presum_runtime]
        arr=[[-2, -1, 0]] #initialized a dummy 
        #Time: N
        for ii, (start, end, duration) in enumerate(tasks):
            #Time: logN
            idx = bisect.bisect_left(arr, [start, 0, 0])
            idx -= 1 # the dummy prevents out-of-bound
            if arr[idx][1] < start:#no overlap
                overlap = arr[-1][2]-arr[idx][2] # the time we can run in parallel
            else:
                overlap = arr[-1][2]-arr[idx][2]+abs(arr[idx][1]-start+1)
            diff = duration - overlap
            curr = end
            while diff > 0:
                if abs(arr[-1][1]-curr) < diff:
                    diff -= abs(arr[-1][1]-curr)
                    curr = arr[-1][0]-1
                    arr.pop()

                else:
                    arr.append([curr-diff+1, end, arr[-1][2]+end-(curr-diff)])
                    diff=0
            return arr[-1][2]