#################
# 20231001
#################

from pprint import pprint as pp
from collections import defaultdict


class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        """
        -> number of k-free subsets  
        g[n%k]
        within group -> sort, DP rob a house problem
        inter group -> multiplication  
        """
        N = len(nums)
        g = defaultdict(list)
        for n in nums:
            g[n % k].append(n)

        def helper(arr):
            if arr is None or len(arr) == 0:
                return 1
            tke = 0
            ntk = 1
            for ii, vv in enumerate(arr):
                if ii == 0:
                    tke = 1
                    ntk = 1
                    continue

                tmp_tke = tke
                tmp_ntk = ntk
                if arr[ii-1]+k == arr[ii]:
                    tke = tmp_ntk
                    ntk = tmp_tke+tmp_ntk
                else:
                    tke = tmp_tke+tmp_ntk
                    ntk = tmp_tke+tmp_ntk
            return tke+ntk

        ans = 1
        for gg, nn in g.items():  # for each group
            nn.sort()
            cnt = helper(nn)
            ans *= cnt
        return ans


########################################


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
