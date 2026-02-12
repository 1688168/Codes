class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        N = len(buildings)
        # we are interested only in turing points and integrating intervals
        # setup diff array framework
        events: DefaultDict[int, List[int]] = defaultdict(list)
        
        # construct all events from buildings
        for [ll, rr, hh] in buildings:
            events[ll].append([hh])
            events[rr].append(-hh)
        
        hh2freq = Counter() # record freq given a hh
        mxh_heap = []        # maintain the max hh given an xx
        ret = []

        # initialize the beginning point
        heappush(mxh_heap, 0)
        hh2freq[0] = 1

        for x in sorted(events):
            for hh in sorted(events[x]):
                if hh > 0: #starting point
                    heappush(mxh_heap, -hh)
                    hh2freq[hh] += 1
                else:
                    hh2freq[hh] -= 1
            
            while mxh_heap and hh2freq[-mxh_heap[0]] == 0: # merge intervals with same height
                heappop(mxh_heap)
            

            ret.append([xx, -mxh_heap[0]]) # record the max hh given an xx

        return ret  