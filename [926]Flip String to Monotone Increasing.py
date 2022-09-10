# A binary string is monotone increasing if it consists of some number of 0's (
# possibly none), followed by some number of 1's (also possibly none). 
# 
#  You are given a binary string s. You can flip s[i] changing it from 0 to 1 
# or from 1 to 0. 
# 
#  Return the minimum number of flips to make s monotone increasing. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "010110"
# Output: 2
# Explanation: We flip to get 011111, or alternatively 000111.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "00011000"
# Output: 2
# Explanation: We flip to get 00000000.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s[i] is either '0' or '1'. 
#  
# 
#  Related Topics String Dynamic Programming 👍 2240 👎 97


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
        : each char has option 0 or 1
        : all combination: 2^N where n is len(s)
        : check if valid and capture min flip
        : couting with options, looking for optimimal solution with min flip
        : => DP
        : dp1[ii]: required flip to make all zero ending with index ii
        : dp2[ii]: required flip to amke all ones startgin with index ii to the end
        : for all ii: find min(dp1[ii]+dp2[ii])
        : => T: O(N), S: O(N)
        """
        N = len(s)
        dp1 = [0] * (N)  # space: O(N)
        dp2 = [0] * (N)

        for ii in range(N):  # time O(N)
            if ii == 0:
                dp1[ii] = (0 if s[ii] == '0' else 1)
            else:
                dp1[ii] = dp1[ii - 1] + (1 if s[ii] == '1' else 0)

        for jj in reversed(range(N)):
            if jj == N - 1:
                dp2[jj] = (0 if s[jj] == '1' else 1)
            else:
                dp2[jj] = dp2[jj + 1] + (1 if s[jj] == '0' else 0)

        ans = float('inf')
        for ii in range(1, N):
            ans = min(ans, dp1[ii - 1] + dp2[ii], dp1[N - 1], dp2[0])
        # return min(ans, dp1[N-1], dp2[0])
        return ans

# leetcode submit region end(Prohibit modification and deletion)
