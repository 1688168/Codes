# The variance of a string is defined as the largest difference between the 
# number of occurrences of any 2 characters present in the string. Note the two 
# characters may or may not be the same. 
# 
#  Given a string s consisting of lowercase English letters only, return the 
# largest variance possible among all substrings of s. 
# 
#  A substring is a contiguous sequence of characters within a string. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "aababbb"
# Output: 3
# Explanation:
# All possible variances along with their respective substrings are listed 
# below:
# - Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", 
# "bb", and "bbb".
# - Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", 
# and "bab".
# - Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
# - Variance 3 for substring "babbb".
# Since the largest possible variance is 3, we return it.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "abcde"
# Output: 0
# Explanation:
# No letter occurs more than once in s, so the variance of every substring is 0.
# 
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s consists of lowercase English letters. 
#  
# 
#  Related Topics Array Dynamic Programming 👍 438 👎 46


"""
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
        def largestVariance(self, s: str) -> int:
            # char instance count is like converting char array to 1,0 array
            # ababab => 101010
            # count of a => subarray sum of 1
            # the diff of two chars is like make a=1, b=-1
            # => max subarray sum anchoring on a -1 to maximize the variance

            # all given chars
            ctr = Counter(s)

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
                nums = [0] * len(s)
                for ii in range(len(s)):
                    if s[ii] == x: nums[ii] = 1
                    if s[ii] == y: nums[ii] = -1

                dp1[0] = nums[0]
                for ii in range(1, len(s)):
                    dp1[ii] = max(dp1[ii - 1] + nums[ii], nums[ii])

                # pp(dp1)
                lmv = float('-inf')
                dp = nums[-1]
                if nums[-1] == -1:
                    lmv = max(lmv, dp1[-1] + dp - nums[-1])
                for ii in reversed(range(len(s) - 1)):
                    dp = max(dp + nums[ii], nums[ii])

                    if nums[ii] == -1:
                        lmv = max(lmv, dp1[ii] + dp - nums[ii])

                mxv = max(lmv, mxv)

            return mxv

# leetcode submit region end(Prohibit modification and deletion)
