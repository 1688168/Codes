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
