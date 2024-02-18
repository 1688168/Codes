from heapq import heappush, heappop, heappushpop
class obj:
    def __init__(self, ww, ff):
        self.word=ww
        self.freq=ff

    def __lt__(self, oo):
        if self.freq==oo.freq:
            return self.word > oo.word
        return self.freq < oo.freq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        - k most frequent strings
        """
        w2f=collections.Counter(words)
        mnq=[]
        
        for ww, ff in w2f.items():
            if len(mnq) < k:
                heappush(mnq, obj(ww, ff))
            else:
                heappushpop(mnq, obj(ww, ff))
        res=[]
        while mnq:
            res.append(heappop(mnq).word)
        
        return reversed(res)