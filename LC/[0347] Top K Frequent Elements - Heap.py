from collections import Counter
from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr=Counter(nums) # o(N)
        mnq=[]

        for kk, vv in ctr.items():# O(Nlogk), space O(K) ==> quick select O(K)
            if len(mnq) < k:
                heappush(mnq, (vv, kk))
            else:
                if vv > mnq[0][0]:
                    heappop(mnq)
                    heappush(mnq, (vv, kk))

        res=[kk for (vv, kk) in mnq]


        return res
