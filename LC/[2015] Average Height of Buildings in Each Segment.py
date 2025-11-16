class Solution:
    def averageHeightOfBuildings(self, buildings: List[List[int]]) -> List[List[int]]:
        N=len(buildings) # num of buildings

        # collect events
        events = collections.defaultdict(lambda: [0, 0]) # dict: key: ts, with default value [cnt, ht]=[0, 0]
        for st, ed, ht in buildings:
            events[st][0] += 1
            events[st][1] += ht
            events[ed][0] -= 1
            events[ed][1] -= ht

        segments=[]
        # calc segments with avg
        currCnt=0
        currHt=0
        for ts, [diffCnt, diffHt] in sorted(events.items()): #how to sort dict keys
            currCnt += diffCnt
            currHt += diffHt
            segments.append([ts, 0 if currCnt==0 else currHt//currCnt])

        res=[]
        ii=0
        while ii < len(segments):
            ts=segments[ii][0]
            avg=segments[ii][1]

            if avg==0: # find st of avg>0
                ii+=1
                continue
            
            st=ts

            jj=ii
            while jj<len(segments) and segments[jj][1]==avg: #same height
                jj+=1
            res.append([st, segments[jj][0], avg])
            ii=jj
        return res   

        """
        ### Background:
        * given list of buildings: [[st, ed, h], ...]
        * output list of non-overlapping intervals of buildings_avg: [[st, ed, h_avg], ...] where [st, ed) is non-inclusive ending, and all buildings in this interval [st, ed) all have same avg height
        * 

        ### Analysis:
        * N=10^5: number of buildings
        ##### Bruteforce
        * for each interval, accumulate height: N*N -> 10^10 -> TLE
        
        ##### target Time-complexity: nlogn -> 10^6
        * given intervals with value that we can accumulate
        * sweepline
        1. convert to events -> N
        2. sort events -> + nlogn
        3. accumulate events and calc avg -> +N
        4. output non-overlapping intervals -> +N
        """ 