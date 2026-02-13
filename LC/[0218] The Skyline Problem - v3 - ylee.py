class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        N = len(buildings)
        # we are interested only in turing points and integrating intervals
        # setup diff array framework
        events: DefaultDict[int, List[int]] = defaultdict(list)
        
        # construct all events from buildings
        for [ll, rr, hh] in buildings:
            events[ll].append(hh)  # starting point
            events[rr].append(-hh) # ending point
        
        hh2freq = Counter({0:1}) # record freq given a hh
        mxh_heap = []        # maintain the max hh given an xx
        ret = []

        # initialize the beginning point
        heappush(mxh_heap, 0)

        for x in sorted(events): #this sorts key (location)
            for hh in sorted(events[x]):
                if hh > 0: #starting point
                    heappush(mxh_heap, -hh)
                    hh2freq[hh] += 1
                else:
                    hh2freq[-hh] -= 1
            
            while mxh_heap and hh2freq[-mxh_heap[0]] == 0: # merge intervals with same height
                heappop(mxh_heap)
            
            if len(ret)==0 or -mxh_heap[0] != ret[-1][1]: #skip turning point with same height
                ret.append([x, -mxh_heap[0]]) # record the max hh given an xx

        return ret  