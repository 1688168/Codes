# Given a string s, find the longest palindromic subsequence's length in s. 
# 
#  A subsequence is a sequence that can be derived from another sequence by 
# deleting some or no elements without changing the order of the remaining elements. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 1000 
#  s consists only of lowercase English letters. 
#  
# 
#  Related Topics String Dynamic Programming 👍 6185 👎 256


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)

        dp = [[0] * (N) for _ in range(N)]

        for ii in range(N):
            dp[ii][ii] = 1

        for ii in reversed(range(N - 1)):
            for jj in range(ii + 1, N):
                if s[ii] == s[jj]:
                    dp[ii][jj] = 2 + dp[ii + 1][jj - 1]
                else:
                    dp[ii][jj] = max(dp[ii][jj - 1], dp[ii + 1][jj])
        # print(dp)
        return dp[0][N - 1]
        
# leetcode submit region end(Prohibit modification and deletion)
