###########
# 20231121
###########
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        - bucket sort
        """
        N = len(nums)
        freq = [[] for _ in range(N+1)]

        n2f = collections.Counter(nums)
        for nn, ff in n2f.items():
            freq[ff].append(nn)

        res = []
        done = False
        for ii, bucket in enumerate(reversed(freq)):
            for n in bucket:
                res.append(n)
                if len(res) == k:
                    done = True
                    break

            if done:
                break

        return res


########################


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        : bucket sort
        : freq=index
        : value is the list of "nums values" in this freq
        """
        N = len(nums)
        buckets = [[] for ii in range(N+1)]  # freq 0, 1, ... N
        ctr = Counter(nums)

        for kk, vv in ctr.items():
            buckets[vv].append(kk)

        res = []
        for ii in reversed(range(len(buckets))):
            res.extend(buckets[ii])
            if len(res) >= k:
                break

        return res[:k]
