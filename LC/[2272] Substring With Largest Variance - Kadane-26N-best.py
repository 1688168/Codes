"""
# diff of count of two char:
- assume the two chars are (a, b)
- the count of diff of the two char is equivalent to let a=1, b=-1 (others 0) and perform subarray sum
- Max subarray sum -> Kadane's algorithm
- if a==b: sum=0 (equal count of 1 and -1)

# any two chars in the sub-array -> have to try all combination
"""

from collections import Counter, defaultdict


"""
The Optimization: since only 1, -1 will affect the total sum, we should skip zeros
"""


class Solution:
    def largestVariance(self, s: str) -> int:
        char2cnt = Counter(list(s))
        chars = list(char2cnt.keys())
        char2idx = defaultdict(list)
        for ii, cc in enumerate(list(s)):
            char2idx[cc].append(ii)

        N = len(chars)
        mxv = -math.inf

        # here we only process the 1, -1s and skip zeros
        for a, a_idx in char2idx.items():  # try all combinations
            for b, b_idx in char2idx.items():
                if a == b:
                    mxv = max(mxv, 0)
                    continue

                # print(" a: ", a, " b: ", b)
                """
                This is modifed Kadane, we need to ensure both a and b are present to update max 
                """
                sum_no_b = 0
                sum_has_b = -math.inf//2
                ii, jj = 0, 0
                while ii < len(a_idx) or jj < len(b_idx):
                    """
                    - we are processing two array of indexs.(from left to right).  
                    - ii, jj whoever is smaller and not out-of-bound should be 
                    processed first (from left to right)
                    """

                    # we need to process the one in the front first
                    if jj >= len(b_idx) or (ii < len(a_idx) and a_idx[ii] < b_idx[jj]):
                        # if b_idx is exhausted or the subarray is ending with a_idx[ii] (are are not @ b yet)
                        # whoever is smaller is the current ending index
                        ii += 1
                        sum_no_b += 1
                        sum_has_b += 1

                    elif ii >= len(a_idx) or (jj < len(b_idx) and b_idx[jj] < a_idx[ii]):
                        jj += 1
                        sum_has_b = max(sum_no_b - 1, sum_has_b-1)
                        sum_no_b = 0

                    mxv = max(mxv, sum_has_b)

        return mxv
