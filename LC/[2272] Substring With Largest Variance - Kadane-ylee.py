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
        char2cnt=Counter(list(s))
        chars=char2cnt.keys()

        N=len(chars)
        for ii in range(N): # try all combinations
            for jj in range(N):



        