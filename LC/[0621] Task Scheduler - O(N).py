from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        1. find max_freq
        2. requied the max(max_freq*N+remaining, ttl_tasks)

        0 1 2 3 ... N  << wait for n so, the column cnt is n+1
        x y z a     v 
        x y z a     idle
        x y z b     idle
        x y z b
        x y z b
        x y z b     ...
        x y
        """
        c2freq = Counter(tasks)
        max_freq = 0
        freq2cnt = collections.defaultdict(int)
        for cc, ff in c2freq.items():
            freq2cnt[ff] += 1
            max_freq = max(max_freq, ff)

        remaining = freq2cnt[max_freq]
        return max((max_freq-1)*(n+1)+remaining, len(tasks))
