###################
# 20231001
###################
from collections import Counter, defaultdict
from collections import defaultdict, Counter


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        g = defaultdict(set)
        for n in nums:
            g[n % k].add(n)
        n2cnt = Counter(nums)

        def helper(arr):
            if arr is None or len(arr) == 0:
                return 1
            arr.sort()
            tke = 0
            ntk = 0
            for ii, vv in enumerate(arr):

                if ii == 0:
                    tke = 1*(pow(2, n2cnt[vv])-1)
                    ntk = 1
                    continue
                tmp_tke = tke
                tmp_ntk = ntk

                if ii > 0 and arr[ii-1]+k == vv:
                    tke = tmp_ntk*(pow(2, n2cnt[vv])-1)
                    ntk = tmp_ntk+tmp_tke
                else:
                    tke = (tmp_tke + tmp_ntk)*(pow(2, n2cnt[vv])-1)
                    ntk = tmp_tke + tmp_ntk
            return tke+ntk

        ans = 1
        for gg, nn in g.items():
            ans *= helper(list(nn))

        return ans-1


###############################################


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
