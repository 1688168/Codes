########
# 
########
from collections import defaultdict
class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        """
        - subsets with no diff of pairs that is k
        - we know how to find all subsets from nums with duplicate number
        - how to avoid adding new member to subset with diff=k?
        a. group nums by mod k
        b. count of subset = g1*g2*... (as each group is mod k, so inter-group will not have diff=k)
        ** given a list, the current decision depends on some relationship with prev element -> house robber
        c. when adding new member to subset, just compare to prev one 
        """
        ans=1
        # group nums by mod k
        g2n=defaultdict(list)
        for n in nums:
            g2n[n%k].append(n)

        def dfs(st, sz, subset, prev):
            nonlocal cnt
            if subset==sz:
                cnt +=1
                return 
            
            for ii in range(st, len(nn)):
                if prev is None or nn[ii]-k!=prev:
                    dfs(ii+1, sz, subset+1, nn[ii])


        # for each group count subset cnt
        for gg, nn in g2n.items():
            nn.sort() # we need to exclude diff k 
            cnt=0
       
            for sz in range(len(nn)+1):        
                dfs(0, sz, 0, None)
            # product of group subset cnt is the final ans
            ans *= cnt

        return ans
############################
from collections import defaultdict
class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        """
        - subsets with no diff of pairs that is k
        - we know how to find all subsets from nums with duplicate number
        - how to avoid adding new member to subset with diff=k?
        a. group nums by mod k
        b. count of subset = g1*g2*... (as each group is mod k, so inter-group will not have diff=k)
        ** given a list, the current decision depends on some relationship with prev element -> house robber
        c. when adding new member to subset, just compare to prev one 
        """
        ans=1
        # group nums by mod k
        g2n=defaultdict(list)
        for n in nums:
            g2n[n%k].append(n)

        def dfs(st, sz, subset):
            nonlocal cnt
            if len(subset)==sz:
                cnt +=1
                return 
            
            for ii in range(st, len(nn)):
                if len(subset)==0 or nn[ii]-k!=subset[-1]:
                    dfs(ii+1, sz, subset+[nn[ii]])


        # for each group count subset cnt
        for gg, nn in g2n.items():
            nn.sort() # we need to exclude diff k 
            cnt=0
            subset=[]
            for sz in range(len(nn)+1):        
                dfs(0, sz, subset)
            # product of group subset cnt is the final ans
            ans *= cnt

        return ans