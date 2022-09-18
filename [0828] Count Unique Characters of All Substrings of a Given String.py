# Let's define a function countUniqueChars(s) that returns the number of unique 
# characters on s. 
# 
#  
#  For example, calling countUniqueChars(s) if s = "LEETCODE" then "L", "T", 
# "C", "O", "D" are the unique characters since they appear only once in s, 
# therefore countUniqueChars(s) = 5. 
#  
# 
#  Given a string s, return the sum of countUniqueChars(t) where t is a 
# substring of s. The test cases are generated such that the answer fits in a 32-bit 
# integer. 
# 
#  Notice that some substrings can be repeated so in this case you have to 
# count the repeated ones too. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "ABC"
# Output: 10
# Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
# Every substring is composed with only unique letters.
# Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
#  
# 
#  Example 2: 
# 
#  
# Input: s = "ABA"
# Output: 8
# Explanation: The same as example 1, except countUniqueChars("ABA") = 1.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "LEETCODE"
# Output: 92
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s consists of uppercase English letters only. 
#  
# 
#  Related Topics Hash Table String Dynamic Programming 👍 1679 👎 228
"""
: Brute-force:
: * all subarrays: Time: O(N^2)
: * count unique chars 1+2+...N => O(N^2)
: =============
: * given a char: it can contribute to the count until same char appear before/after the curr char
: * contribution for this char: ii-prev_ii + next_ii - ii
: 1. prepare lookup table
:  + for each uppercase English letter. prefix with -1, suffix with N
:  + traverse the string and update letter occurance
: 2. for each upper case English letter, accumulate each letter's contribution
:
: ========
: 9/3/22
: ========
: 1. For those limiting string with only english letters.  Think about constructing all potential space out of the 26
:    chars.  ex: all pairs, all distinct chars, etc.
: 2. prepare the lookup statistics.  In this example, locations of where the char appears in the string.
: 3. Trick: since we need to calc dist to edge (begin or end), we prefix "-1", and "N" in the lookup array
: 4. construct the lookup table: for each Char, append all locations:
     ex: [-1, 0, 3, 7, len(s)-1]
          ^^           ^^^^^^^^
          prefix       sufix
: 5. contribution of each char:   (loc[ii]-loc[ii-1]) * (loc[ii+1]-loc[ii])
"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # collect location info
        lookup = [[-1] for _ in range(26)]
        for ii, cc in enumerate(s):
            # print("ii: ", ii, " cc: ", cc)
            loc = ord(cc) - ord('A')
            lookup[loc].append(ii)

        for ii in range(26):
            lookup[ii].append(len(s))

        cnt = 0
        for ii in range(26):
            for jj in range(1, len(lookup[ii]) - 1):
                cnt += ((lookup[ii][jj] - lookup[ii][jj - 1]) * (lookup[ii][jj + 1] - lookup[ii][jj]))

        return cnt
        
# leetcode submit region end(Prohibit modification and deletion)
