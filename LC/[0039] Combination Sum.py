##################
# 20240215
##################
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        * candidates: distinct
        * target:
        # Bruteforce: all 

        """
        N=len(candidates)

        def dfs(st, path, curr_ttl):
            if curr_ttl==target:
                res.append(path[:])
                return
            if curr_ttl > target: return

            for ii in range(st, N):
                dfs(ii, path+[candidates[ii]], curr_ttl+candidates[ii])

        res=[]
        path=[]
    
        dfs(0, path, 0)

        return res


###########
# 20230603
###########

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        N = len(candidates)
        def dfs(st, target, path):
            if target==0:
                ans.append(path[:])
                return
            if st >= N: return
            if target < 0: return

            for ii in range(st, N):
                dfs(ii, target-candidates[ii], path+[candidates[ii]])

        path=[]
        dfs(0, target, path)

        return ans
        



###########################

from functools import lru_cache
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        M=len(candidates)
        N=target
        def dp(st, tgt, path):
            if tgt==0:
                res.append(path[:])
                return

            if st < 0 or st >= M: return
            if tgt < 0 or tgt > N: return

            for ii in range(st, M):
                dp(ii, tgt-candidates[ii], path+[candidates[ii]])

        path=[]
        dp(0, target, path)

        return res
