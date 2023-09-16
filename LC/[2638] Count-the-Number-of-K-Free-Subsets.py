from collections import defaultdict
from pprint import pprint as pp


class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        N = len(nums)
        grp = defaultdict(set)
        for n in nums:
            grp[n % k].add(n)

        def helper(g):
            take = 0
            notake = 1
            g.sort()
            for ii in range(len(g)):
                tmp_take = take
                tmp_notake = notake

                if ii > 0 and g[ii-1]+k == g[ii]:
                    take = tmp_notake
                    notake = tmp_notake+tmp_take
                else:
                    take = tmp_take+tmp_notake
                    notake = tmp_take+tmp_notake
            return take+notake

        res = 1
        for kk, gg in grp.items():
            res *= helper(list(gg))

        return res
