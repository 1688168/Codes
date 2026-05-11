class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        * when dealing with intervals. (start, end) all represent events. -> sweepline
        """
        # build all events
        events=[]
        for ss, ee in intervals:
            events.append((ss, 1))
            events.append((ee, -1))
        
        # sort event start first
        events.sort(key=lambda x: (x[0], -x[1])) # for same position, start with higher priority

        # iterating over events, and output block when cnt=0 (no more overlapping blocks)
        start=0
        cnt=0

        res=[]
        for xx, delta in events:
            if cnt==0: #currently no block, starting a new block
                start=xx
            
            cnt += delta # always accumulating counter

            if cnt == 0: # when counter hit zero -> we finished a blcok
                res.append([start, xx]) # output the block

        return res
        