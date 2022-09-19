from heapq import heappush, heappop
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # greedy, attend the one starts the first and add all those available to a PQ.
        # the next day. add newly available events into PQ, evict those expired.
        # pop the top one in PQ to attend and continue

        max_day=pow(10, 5)+1
        mnq=[]
        events.sort() # sort by st, ed in increasing order
        ii=0
        cnt=0
        for day in range(1, max_day):
            while ii < len(events) and events[ii][0]<= day:
                heappush(mnq, events[ii][1])
                ii+=1
            
            while len(mnq) > 0 and mnq[0] < day:
                heappop(mnq)

            if len(mnq) > 0:
                cnt += 1
                heappop(mnq)

        return cnt
