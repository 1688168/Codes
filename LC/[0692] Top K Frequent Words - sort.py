class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        w2f=collections.Counter(words)
        wf=[(f, w) for w, f in w2f.items()]
        wf.sort(key=lambda x: (-x[0], x[1]))

        res=[w for (f, w) in wf[:k]]
        
        return res