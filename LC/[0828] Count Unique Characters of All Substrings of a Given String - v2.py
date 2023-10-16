"""
# 20230923
"""
from collections import defaultdict


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """
        c x x c x x x x c
              i
        a                b
        c will contribute (i-a)(b-i)
        """

        N = len(s)
        c2idx = defaultdict(list)
        for ii, vv in enumerate(s):
            c2idx[vv].append(ii)

        ttl = 0
        for cc, vv in c2idx.items():  # looping by char instead by the string
            vv = [-1]+vv+[N]  # insert dummy in beginning and ending
            for jj in range(1, len(vv)-1):  # starting from 1 as prev is dummy
                a = vv[jj]-vv[jj-1]
                b = vv[jj+1]-vv[jj]
                ttl += a*b
        return ttl


"""
# 20221018
"""


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """
        * all substrings: O(N^2)
        * each time we are asked for aggregate some metrics from subarray
        -> evaluate each element's contribution to the final answer
        -> pre-calculate the required inputs for evaluating individual char's contribution
        -> evaluate if we can improve time complexity
        -------
        * for each char, what's it's contribution to subarray unique char sum?
        * A1 x x x A2 x x x A3
          ^^^^^^^^
          0  1 2 3
             ^^^^^    ^^^^^
                      5 6 7

        + precalc all char's location
        + A1's contribution to final answer is 4
        + A2's contribution: left_cnt*right_cnt
        """
        N = len(s)
        # find location of all chars
        char2locs = defaultdict(list)
        # prefix -1 for convience
        for c in s:
            char2locs[c].append(-1)
        for ii, c in enumerate(s):
            char2locs[c].append(ii)
        # sufix N for convience
        for c in s:
            char2locs[c].append(N)

        # calc contribution of each char
        res = 0

        for c, locs in char2locs.items():
            for ii in range(1, len(locs)-1):
                res += (locs[ii]-locs[ii-1])*(locs[ii+1]-locs[ii])
        return res
