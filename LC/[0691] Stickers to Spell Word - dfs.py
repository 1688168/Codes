from collections import Counter
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        sticker_dict_lst=[]
        for sticker in stickers:
            sticker_dict_lst.append(Counter(sticker))

        memo={}
        def dfs(target, sticker_dict):
            if target in memo: return memo[target]

            res = 1 if sticker_dict else 0
            rest=""
            for cc in target:
                if cc in sticker_dict and sticker_dict[cc] > 0:
                    sticker_dict[cc]-=1
                else:
                    rest += cc
            
            if rest:
                used = math.inf
                for sticker_dict in sticker_dict_lst:
                    if rest[0] not in sticker_dict: continue
                    used = min(used, dfs(rest, sticker_dict.copy()))
                memo[rest]=used
                res += used
            return res  

        res = dfs(target, {})
        return res if res != math.inf else -1
        