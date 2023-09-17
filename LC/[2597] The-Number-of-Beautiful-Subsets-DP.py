from collections import Counter, defaultdict


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        val2cnt = Counter(nums)

        grps = defaultdict(set)

        for n in nums:
            grps[n % k].add(n)

        res = 1
        for gid, g in grps.items():
            glist = sorted(list(g))
            take = 0
            no_take = 1

            for ii, vv in enumerate(glist):
                tmp_take = take
                tmp_no_take = no_take
                if ii > 0 and glist[ii-1]+k == vv:
                    take = tmp_no_take * (pow(2, val2cnt[vv])-1)
                    no_take = (tmp_take+tmp_no_take)*1
                else:
                    take = (tmp_take+tmp_no_take) * (pow(2, val2cnt[vv])-1)
                    no_take = (tmp_take+tmp_no_take)*1

            res *= (take+no_take)

        return res-1
