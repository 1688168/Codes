from collections import Counter

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        stkr_lst = [Counter(sticker) for sticker in stickers]

        memo={} #given a target, return the min num of stickers required to spell-out
        def dfs(target, stkr):
            if target=="" or target is None: return 0 # no target to match, no sticker required 
            if target in memo: return memo[target]
            res=1 if stkr else 0#current sticker is not Null
            # exhausting current sticker
            rests=""
            for cc in target: #check each cc in target see if current sticker has it
                if cc not in stkr:
                    rests+=cc
                else:
                    stkr[cc]-=1
                    if stkr[cc]==0: del stkr[cc]
            
            # recursion
            if rests:
                other=math.inf
                for stkr in stkr_lst:
                    if rests[0] not in stkr: continue
                    other = min(other, dfs(rests, stkr.copy()))
                memo[rests]=other
                res+=other
      
            return res


        res = dfs(target, {})

        return res if res != math.inf else -1
        
##############
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
        