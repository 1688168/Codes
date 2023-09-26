"""
# diff of count of two char:
- assume the two chars are (a, b)
- the count of diff of the two char is equivalent to let a=1, b=-1 (others 0) and perform subarray sum
- Max subarray sum -> Kadane's algorithm
- if a==b: sum=0 (equal count of 1 and -1)

# any two chars in the sub-array -> have to try all combination
"""
from collections import Counter


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

                # print(" a: ", a, " b: ", b)
                sum_no_b = 0
                sum_has_b = -math.inf//2
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