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
