################
# 20240609-1
################
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        * given a list of resource
        * given capacity limination on list of resource
        => max of resources you can carry
        ==> knapsack:
        ** standard knapsack problem:
        + each resource has weight
        + each resource is take or no-take
        + limitation on total weight
        + max profit you can carry
        
        ** target sum
        + all items need to be select but with addition or substraction
        + constrain is total sum
        """
        rcs=[]
        N=len(strs)
        for ss in strs:
            zz=0
            oo=0
            for cc in ss:
                if cc=='0': zz+=1
                if cc=='1': oo+=1
            rcs.append((zz, oo))
        
        @cache
        def dfs(st, mm, nn):
            if st >= N: return 0
        
            tke=0
            if rcs[st][0] <= mm and rcs[st][1] <= nn:
                tke = 1+dfs(st+1, mm-rcs[st][0], nn-rcs[st][1])
            
            ntk=dfs(st+1, mm, nn)
        
            return max(tke, ntk)            
        

        return dfs(0, m, n)

################
# 20240609-2
################
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        * given a list of resource
        * given capacity limination on list of resource
        => max of resources you can carry
        ==> knapsack:
        ** standard knapsack problem:
        + each resource has weight
        + each resource is take or no-take
        + limitation on total weight
        + max profit you can carry
        
        ** target sum
        + all items need to be select but with addition or substraction
        + constrain is total sum
        """
        rcs=[]
        N=len(strs)
        for ss in strs:
            zz=0
            oo=0
            for cc in ss:
                if cc=='0': zz+=1
                if cc=='1': oo+=1
            rcs.append((zz, oo))
        
        @cache
        def dfs(st, mm, nn, cnt):
            if st >= N: return cnt
        
            tke=0
            if rcs[st][0] <= mm and rcs[st][1] <= nn:
                tke = dfs(st+1, mm-rcs[st][0], nn-rcs[st][1], cnt+1)
            
            ntk=dfs(st+1, mm, nn, cnt)
        
            return max(tke, ntk)            
        

        return dfs(0, m, n, 0)


#######################
from functools import lru_cache
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        nstrs=[]
        for s in strs:
            ones=0
            zeros=0
            for c in s:
                if ord(c)-ord('0') == 0:
                    zeros += 1
                else:    
                    ones += 1
            
            nstrs.append([zeros, ones])
            
        #print("nstrs: ", nstrs)
        @lru_cache(None)
        def hp(st=0, mm=m, nn=n):
            if st >= n: return 0
            
            tke=0
            zz=nstrs[st][0]
            oo=nstrs[st][1]
            
            if zz <= mm and oo <= nn:
                tke = 1+hp(st+1, mm-zz, nn-oo)
            
            ntk=hp(st+1, mm, nn)
            
            return max(tke, ntk)
        
        
        n=len(nstrs)
        ans=hp()
        return ans
                
        