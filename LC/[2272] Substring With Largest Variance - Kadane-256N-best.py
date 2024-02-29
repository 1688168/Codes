##############
# 20240229
##############
from collections import Counter


class Solution:
    def largestVariance(self, s: str) -> int:
        """
        * lowercase english -> combination of chars: 26*26
        * diff of count of two chars -> let a=1, b=-1, others=0
        => Largest variance -> largest subarray sum -> modified Kadane (need both (a, b) in the subarray)
        """

        # get all in scope chars
        chars = set([c for c in s])
        # try all combination of chars
        ans = -math.inf
        for a in chars:
            for b in chars:
                if a == b:
                    continue  # need two chars
                # for each combination (a, b) -> mondified Kadane
                dp0 = 0  # largest subarray sum ending @ ii containing b
                dp1 = -math.inf//2  # largest subarray sum ending @ ii not containing b
                for c in s:
                    tmp0 = dp0
                    tmp1 = dp1
                    if c not in (a, b):
                        continue
                    if c == a:
                        dp0 = tmp0+1
                        dp1 = tmp1+1
                    else:
                        dp0 = max(tmp0-1, tmp1-1)
                        dp1 = 0

                    ans = max(ans, dp1)

        return ans


####################################
"""
# diff of count of two char:
- assume the two chars are (a, b)
- the count of diff of the two char is equivalent to let a=1, b=-1 (others 0) and perform subarray sum
- Max subarray sum -> Kadane's algorithm
- if a==b: sum=0 (equal count of 1 and -1)

# any two chars in the sub-array -> have to try all combination
"""


class Solution:
    def largestVariance(self, s: str) -> int:
        char2cnt = Counter(list(s))
        chars = list(char2cnt.keys())

        N = len(chars)
        mxv = -math.inf
        for ii in range(N):  # try all combinations
            for jj in range(N):
                a = chars[ii]
                b = chars[jj]
                if a == b:
                    mxv = max(mxv, 0)
                    continue
                """
                Note: since we need to find the diff of two frequency, we need to ensure the max subarray sum contains
                      both (a,b)=(1, -1), so the DP function is not same as regular Kadane
                """
                """
                round (ii)     state(jj=(0, 1))                
                1              contains b(-1)           not contain b (-1)
                2
                3
                4
                return max(contains b)
                """

                # print(" a: ", a, " b: ", b)
                sum_no_b = 0  # when we have nothing, and not having -1
                sum_has_b = -math.inf//2  # when we have nothing and need to have -1 -> invalid
                for idx, cc in enumerate(list(s)):
                    # print(" cc: ", cc)
                    if cc == a:  # cc is current value
                        sum_no_b += 1
                        sum_has_b += 1
                    elif cc == b:
                        sum_has_b = max(sum_no_b - 1, sum_has_b-1)
                        sum_no_b = 0

                    mxv = max(mxv, sum_has_b)

        return mxv
