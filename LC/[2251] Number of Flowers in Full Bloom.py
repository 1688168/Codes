class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        N = len(flowers) # total num of intervals
        events = defaultdict(int) # data model to record events

        # convert to events
        for st, ed in flowers: # collecting events
            events[st] += 1
            events[ed+1] -= 1 # interval is inclusive
        
        cnts=0
        ans=[0]*len(people)
        events_sorted = sorted(events.items())
        people_sorted = sorted(enumerate(people), key=lambda x: x[1])
        st=people_sorted[0][0]
        print(people_sorted)

        # for each people, we need to know the accumulated cnt
        jj=0
        for idx, ts in people_sorted:
            while jj<len(events_sorted) and events_sorted[jj][0] <=ts:
                cnts += events_sorted[jj][1]
                jj+=1
            
            ans[idx] = cnts
        
        return ans




        