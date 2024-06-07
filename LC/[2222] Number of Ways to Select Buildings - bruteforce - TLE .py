###########
# 20240606
###########
class Solution:
    def numberOfWays(self, s: str) -> int:
        N=len(s)
        def dfs(prev, st, cnt):
            if cnt==3:
                return 1
            
            if st >= N:
                return 0
            
            ttl=0
            for ii in range(st, N):
                if prev is None:
                    ttl += dfs(ii, ii+1, cnt+1)
                else:
                    if s[ii] != s[prev]:
                        ttl += dfs(ii, ii+1, cnt+1)
        
            return ttl

        return dfs(None, 0, 0)
        

########
# 20240605
########
class Solution:
    def numberOfWays(self, s: str) -> int:
        """
        # I/O:
        + s: '0' - office
             '1' - restaurant
        => number of valid ways to select 3 buildings

        # Analysis:
        + N=10^5 

        > Bruteforce
        > DP
        """
        N=len(s)
        def dfs(prev, st, selected):
            nonlocal ttl
            
            if selected==3:
                ttl+=1
                return
            if st >=N: return
            
            for ii in range(st, N):
                if prev is not None and s[ii] == s[prev]: continue
                dfs(ii, ii+1, selected+1)
        ttl=0
        dfs(None, 0, 0)
        return ttl
        



####################
class Solution:
    def numberOfWays(self, s: str) -> int:

        def dfs(sz, st, path):
            nonlocal cnt
            if len(path) == 3:
                cnt += 1
                return
            if len(path) > 3:
                return

            for ii in range(st, N):
                if len(path) > 0 and s[ii] == path[-1]:
                    continue
                dfs(sz, ii+1, path+[s[ii]])

        N = len(s)
        cnt = 0     
        path = []
        dfs(3, 0, path)
        return cnt
