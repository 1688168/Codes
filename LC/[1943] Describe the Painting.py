from collections import defaultdict
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        N=len(segments) # how many intervals
        events = defaultdict(int) #default value to int

        # converting intervals to events (ts, cnt)
        for st, ed, ct in segments:
            events[st] = events.get(st, 0) + ct
            events[ed] = events.get(ed, 0) - ct


        res=[]
        acc=0
        st=-1
        for ts, cnt in sorted(events.items(), key=lambda x: x[0]):
            if st==-1: #we have a new start
                st=ts
            else: #we have an end
                res.append([st, ts, acc])
                st=ts
            acc += cnt
            if acc==0: st=-1

        return res

"""
# Given
* intervals (overlapping, non-inclusive) with unique colors
* implying after merging, the color still unique (not very clear on 
this, but it is working)

# Ask
* merge intervals and aggregate colors. output min intervals with unique color

# Analysis
* interval with value to aggregate -> sweepline
1. convert intervals to events 
2. to maintain order, we need to use ordered map or sort the collection
3. aggregate events to merged intervals
4. if required, merge intervals with same aggregated values
"""