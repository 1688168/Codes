"""
: => largest Variance among all substrings
: Bruteforce:
: 1. all substrings: O(N^2) where N=10^4
: 2. calc variance for each subarray O(N)
: ----------
: # High level strategy:
: * complexity analysis and strategy
: ** only dealing with 26 chars
: ** all pairs = C26, 2 = 26*25/(2*1)=325
: ** length=10^4
:
: # Heuristics:
: * count of char: "sum of subarray by replacing that char as 1 and others 0"
: * count diff btn two char: set one char as 1, the other as -1, and others as zero
: * max count diff => one -1, all others 1s
: * max subarray sum => kadane's algorith
: ----------
: # when you see Subarray sum
: a. presum
: b. kadane (max subarray sum algorithm)
: ----------
1. get all pairs from 26 chars
2. construct 1, -1, 0 representation
3. left/right kadane's algorithm centering on -1 and capture local max
4. update global max for all pairs
5. output global max
: ----------
: ----------
: 1. only lowercase English letters (we can construct all potential pairs: C(26,2))
: 2. Largest variance possible: all substring, all variance
: 3. bruteforce: all substring: T: N^2 + all variance of each substring -> find the local max -> global max
: ----------
: => construct all pairs of unique chars in the string: T: O(M^2)
: => for each pair of chars (a, b), convert the string from (a, b, x) => (1, -1, 0)
: ex: a  b  c d e
:     1 -1  0 0 0
: => max subarray sum centered on "-1": max_subarray_sum_left on "-1" and max_subarray_sum_rigth on "-1" - (-1)//duplicate count
: => above is the max variance of pair (a, b)
: => calc max variance for all pairs
: => output the global max variance among all pairs
: Time: all pairs: O(m^2) //where m is the unique char count of the string
: kadane's alg (left, right): 2*O(N)
:
"""
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def largestVariance(self, s: str) -> int:
        # char instance count is like converting char array to 1,0 array
        # ababab => 101010
        # count of a => subarray sum of 1
        # the diff of two chars is like make a=1, b=-1
        # => max subarray sum anchoring on a -1 to maximize the variance

        # all given chars
        ctr = Counter(s) # O(N)

        mxv = 0
        # construct all potential pairs of the given chars
        chrs = [k for k in ctr.keys()]
        # chrs.sort()
        pairs = []
        for ii in range(len(chrs)):
            x = chrs[ii]
            for jj in range(len(chrs)):
                if ii == jj: continue
                y = chrs[jj]
                pairs.append((x, y))

        # pp(pairs)
        dp1 = [0] * len(s)
        # dp2=[0]* len(s)
        dp = 0

        for x, y in pairs:  # traverse each pair
            nums = [0] * len(s)  # make up the 1,0 -1 array
            for ii in range(len(s)):
                if s[ii] == x: nums[ii] = 1
                if s[ii] == y: nums[ii] = -1
            # dp1 is subarray sum ending @ ii
            dp1[0] = nums[0] # setup for Kadane's algorithm for max subarray sum
            for ii in range(1, len(s)):
                dp1[ii] = max(dp1[ii - 1] + nums[ii], nums[ii])

            # pp(dp1)
            lmv = float('-inf')

            # dp is max subarray sum from right, reduced to single var
            dp = nums[-1]
            if nums[-1] == -1: # reversed kadane's algorithm
                lmv = max(lmv, dp1[-1] + dp - nums[-1])

            for ii in reversed(range(len(s) - 1)): #going reversed
                dp = max(dp + nums[ii], nums[ii])

                if nums[ii] == -1:#centering on -1 for max variance
                    lmv = max(lmv, dp1[ii] + dp - nums[ii])

            mxv = max(lmv, mxv)

        return mxv

# leetcode submit region end(Prohibit modification and deletion)
