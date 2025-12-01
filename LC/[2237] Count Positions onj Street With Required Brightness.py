class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        # convert interval to events
        events=defaultdict(int)
        for (pp, range) in lights:
            st = max(0, pp-range)
            ed = min(n-1, pp+range)+1
            events[st] +=1
            events[ed] -=1
        
        events_sorted = sorted(events.items())
        # For each requirements, check if satisfy requirement and accumulate count
        ans=0
        cnt=0
        jj=0
        for (pp, req) in enumerate(requirement):
            while jj<len(events_sorted) and events_sorted[jj][0] <= pp:
                cnt += events_sorted[jj][1]
                jj+=1
            
            if cnt >= req: ans += 1

        return ans



# ### Given:
# * n: requirement[ii]: min birghtness @ ii
# * lights[ii] = [idxi, range] --- covers idx+/-range #inclusive
# * brightness: accumulated lamp count

# ### Analysis:
# * n=10^5 -> nlon
# ##### Bruteforce
# * calculate accumulated brightness: n*n->TLE

# ##### sweepline
# * intervals aggregation