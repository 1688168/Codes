###############
# 20240218
###############
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        # bucket sort
        - array of size N: -> max freq is N
        """
        N=len(words)
        buckets=[[] for _ in range(N+1)]

        w2f=collections.Counter(words)
        for w, f in w2f.items():
            buckets[f].append(w)
        res=[]
        done=False
        for ii in reversed(range(N+1)):
            b=buckets[ii]
            b.sort()
            for n in b:
                res.append(n)
                if len(res)==k: 
                    done=True
                    break
            
            if done: break
        
        return res

##############
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        # bucket sort
        """
        ctr=Counter(words)
        N=len(words)
        buckets=[[] for _ in range(N+1)]

        for kk, vv in ctr.items():
            buckets[vv].append(kk)

        res=[]
        for ii in reversed(range(len(buckets))):
            for w in buckets[ii]:
                res.append((ii, w))
            if len(res) >=k: break

        res.sort(key=lambda x: (-x[0], x[1]))

        return [v for (k, v) in res][:k]
