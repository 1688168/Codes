
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        N=len(s)

        if s[0] != '0' or s[-1] != '0': return False

        reachable=[False]*N
        reachable[0]=True

        next_start = 0
        for ii, vv in enumerate(s):
            #print("ii: ", ii, " reachable: ", reachable)
        
            if not reachable[ii] or vv!='0': continue
            
            min_next = max(ii+minJump, next_start)
            max_next = min(ii+maxJump, N-1)

            for jj in range(min_next, max_next+1):
                if s[jj]=='0': reachable[jj]=True
            next_start = max(next_start, max_next+1)
            if reachable[-1]: return True

        return reachable[-1]